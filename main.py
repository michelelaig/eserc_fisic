from datetime import datetime, timedelta
from random import choice
import json
import pretty_errors


def get_done_yesterday_today(lines):
    if yesterday_date in lines:
        yesterday_line = lines.index(yesterday_date)
        if today_date in lines:
            did_yest = lines[yesterday_line + 1:today_line]
        else:
            did_yest = lines[yesterday_line + 1::]
    else:
        did_yest = []

    if today_date in lines:
        today_line = lines.index(today_date)
        did_today = lines[today_line::]
    else:
        did_today = []
    did_to = [s.replace(" dubbio", "") for s in lines if current_year not in s]
    return did_to, did_yest, did_today


def get_last_index(lst, search_string):
    if search_string not in lst:
        return -1
    last_index = len(lst) - lst[::-1].index(search_string) - 1
    return last_index


def get_dubbi(lines):
    dubbi = list(set([s for s in lines if "dubbio" in s]))
    dubbi_last = {d: get_last_index(lines, d) for d in dubbi}

    dubbi_str = [d.replace(" dubbio", "") for d in dubbi]
    dubbi_str_last = {d: get_last_index(lines, d) for d in dubbi_str}

    out = []
    for d in dubbi:
        if dubbi_last[d] > dubbi_str_last[d.replace(" dubbio", "")]:
            out.append(d)
    return out


def calculate_media(lines, dates):
    media = 0
    if lines:
        media = (len(lines) - len(dates)) / (
            (datetime.now() - datetime.strptime(dates[0], "%Y-%m-%d")).days)
    return media


def choose_cap():
    cs = list(diz.keys()) + cap_preferiti * 10
    for t_cap in diz.keys():
        e_t_cap = diz[t_cap]
        esr_rim = e_t_cap["n_esr_max"] - e_t_cap["n_esr"]
        esm_rim = e_t_cap["n_esm_max"] - e_t_cap["n_esm"]
        # print(f"{t_cap}: esr {esr_rim}, esm: {esm_rim}")
        cs.extend(t_cap * (esr_rim + esm_rim))
    cap = choice(list(cs))
    return cap


def occurences(ex, ex_occ, max_occ, dubbi):
    if ex in did_today:
        return 0
    if f"{ex} dubbio" in did_today:
        return 0
    if f"{ex} dubbio" in dubbi:
        return max_occ
    return 1 + max_occ - ex_occ


def choose_ex(cap):
    if dubbi_yest:
        return dubbi_yest[0].replace(" dubbio", "")
    t_cap = diz[cap]

    last_esr = t_cap["n_esr"]
    last_esm = t_cap["n_esm"]

    doable = [f"{cap} esr {1 + i}" for i in range(last_esr)]
    doable.extend([f"{cap} esm {1 + i}" for i in range(last_esm)])

    doable_occ = {s: did_tot.count(s) for s in doable}
    max_occ = 1
    if doable_occ:
        max_occ = max(doable_occ.values()) + 1

    poss = []
    for ex in doable:
        check_last = False
        tmp = [ex] * occurences(ex, doable_occ[ex], max_occ, dubbi)
        if ex == last_esr or ex == last_esm:
            tmp *= 3
        poss.extend(tmp)

    ex = choice(poss)
    return choice(poss)

def resolve(es, c, info):
    cap, tipo, numero = es.split(" ")[0], es.split(" ")[1], es.split(" ")[2]
    feedback = input(f"Ora l'es {c}{es} {info}{ENDC}\n")
    if feedback == "no":
        print("niente")
        exit()
    else:
        if int(numero) == diz[cap][f"n_{tipo}"] and int(numero) < diz[cap][f"n_{tipo}_max"]:
            diz[cap][f"n_{tipo}"] += 1
    with open(done_path, "a") as f:
        if today_date not in dates:
            print(today_date, file=f)
        print(f"{es} {feedback if feedback=='dubbio' else ''}", file=f)
    with open(json_path, "w") as f:
        json.dump(diz, f)
#


def main_exec():

    print(f"La media giornaliera è {media:.2f}")
    print(f"Con questo ne fai {len(did_today)+1}")



    cap = choose_cap()
    ex = choose_ex(cap)
    col = ENDC
    # ex = "7 esr 4"
    cap, tipo, numero = ex.split(" ")[0], ex.split(" ")[1], ex.split(" ")[2]
    info = ""
    if f"{ex} dubbio" in dubbi_yest:
        col = WARNING
        info = "dubbio di ieri"
    elif f"{ex} dubbio" in dubbi:
        col = OKBLUE
        info = "dubbio"
    elif int(numero) == diz[cap][f"n_{tipo}"]:
        col = OKCYAN
        info = ", si procede"

    resolve(ex, col, info)
#


OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

if __name__ == "__main__":
    current_year = datetime.now().strftime("%Y")
    today_date = datetime.now().strftime("%Y-%m-%d")
    yesterday_date = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday_date.strftime("%Y-%m-%d")
    json_path = "_es.json"
    done_path = "_done.csv"

    with open(json_path, "r") as f:
        diz = json.load(f)

    cap_preferiti = ["4", "7"]

     # print(f"Today date: {today_date}, yesterday date: {yesterday_date}")
    with open(done_path, "r") as f:
        lines = [s.strip() for s in f.readlines()]

    dates = [s for s in lines if current_year in s]
    media = calculate_media(lines, dates)
    did_tot, did_yest, did_today = get_done_yesterday_today(lines)

    dubbi = get_dubbi(lines)
    dubbi_yest = [s for s in did_yest if "dubbio" in s and s in dubbi]

    main_exec()
