from datetime import datetime
from random import choice
import json
import pretty_errors


class b:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[96m'


with open("es.json", "r") as f:
    diz = json.load(f)
tipo = choice(["esr", "esr", "esm"])

t = str(datetime.date(datetime.now()))
with open("done.csv", "r") as f:
    lst = f.readlines()
    date = [s.strip() for s in lst if "2024" in s]

    dubbi = [s.strip(" dubbio\n") for s in lst
             if "dubbio" in s and not s.strip(" dubbio\n") + "\n" in lst]
    fatti = [s.strip(" dubbio\n").strip() for s in lst if "2024" not in s]
    fatti_diz = {f: fatti.count(f) for f in fatti}
    if len(fatti_diz):
        m = max(fatti_diz.values())
    else:
        m = 1
    fatti_oggi = []
    if t + '\n' in lst:
        fatti_oggi = [s.strip() for s in lst[lst.index(t + '\n') + 1::]]

cap_preferiti = ["4", "6"]
lista_possibilita = []


def occorrenze(s):
    if s in fatti_oggi:
        # print(f"{s} in fatti_oggi")
        return m + 1
    if s in dubbi:
        # print(f"{s} in dubbi")
        return 0
    if s in fatti_diz:
        return fatti_diz[s]
    return 0


while not lista_possibilita:
    cs = list(diz.keys()) + cap_preferiti * 10
    capitolo = choice(list(cs))
    lista_possibilita = [
        f"{tipo} {i}" for i in range(1, 1 + int(diz[capitolo][f"n_{tipo}"]))
        for j in range(m - occorrenze(f"{capitolo} {tipo} {i}"))]
# print(lista_possibilita)
lista_possibilita.extend([lista_possibilita[- 1]] * 20)

#

#

if date:
    media = (
        len(fatti) /
        (datetime.now() - datetime.strptime(date[0], "%Y-%m-%d")).days
    )
else:
    media = 0

es = choice(lista_possibilita)
n = int(es.split(" ")[1])
if f"{capitolo} {es}" in dubbi:
    c = b.OKGREEN
elif n >= diz[capitolo][f"n_{tipo}"] and n < diz[capitolo][f"n_{tipo}_max"]:
    c = b.OKCYAN
else:
    c = b.OKBLUE

e = b.ENDC

print(f"Con questo ne fai {1 + len(fatti_oggi)},", end=" ")
print(f"la media è {media:.2f} al giorno")

feedback = input(f"Ora facciamo il {c} {es} del capitolo {capitolo} {e}\n")
if feedback == "no":
    print("niente")
    exit()


with open("done.csv", "a") as f:
    if t not in date:
        print(t, file=f)
    print(f"{capitolo} {es} {feedback if feedback=='dubbio' else ''}", file=f)

n = int(es.split(" ")[1])
if n >= diz[capitolo][f"n_{tipo}"] and n < diz[capitolo][f"n_{tipo}_max"]:
    print("Si progredisce verso l'infinito :)")
    diz[capitolo][f"n_{tipo}"] += 1

with open("es.json", "w") as f:
    json.dump(diz, f)
