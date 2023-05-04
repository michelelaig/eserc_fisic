from datetime import datetime
from random import choice
import json
#cap_es = {1 :33,2 :27, 3:43, 4:27,5 : 0}
with open("es.json","r") as f:
	diz = json.load(f)
#print(diz)

#capitolo = "1"
#print(capitolo)

tipo = choice(["esr","esr"])#,"esm"])

t = str(datetime.date(datetime.now()))
with open("done.csv","r") as f:
	lst = f.readlines()
	date  = [s.strip() for s in lst if "2023" in s]
		
	dubbi = [s.strip(" dubbio\n") for s in lst if "dubbio" in s and not s.strip(" dubbio\n")+"\n" in lst]
	fatti = [s.strip(" dubbio\n"). strip() for s in lst if "2023" not in s]
	#print(dubbi)
	#print(fatti)
	fatti_diz = {f : fatti.count(f) for f in fatti}
	m = max(fatti_diz.values())
	fatti_oggi = []
	if t+'\n' in lst:
		fatti_oggi = [s.strip() for s in lst[lst.index(t+'\n')+1::]]
cap_preferiti = ["4","5"]
lista_possibilita = []

def occorrenze(s):
	if s in fatti_oggi:
		return m+1
	if s in dubbi:
		return 0
	if s in fatti_diz:
		return fatti_diz[s]
	return 0

while not lista_possibilita:
	cs = list(diz.keys())+cap_preferiti*10
	capitolo = choice(list(cs))
	lista_possibilita = [f"{tipo} {i}" for i in range(1,1+int(diz[capitolo][f"n_{tipo}"]))for j in range(m-occorrenze(f"{capitolo} {tipo} {i}"))  ]
	lista_possibilita.extend([lista_possibilita[-1]]*9)





media = (
	len(fatti) / (datetime.now() - datetime.strptime(date[0], "%Y-%m-%d")).days
)

#print(lista_possibilita)
es = choice(lista_possibilita)
feedback = input(f"Con questo ne fai {1+len(fatti_oggi)}.\nLa media è di {media} al giorno, ora facciamo il {es} del capitolo {capitolo}\n")
if feedback=="no":
	print("niente")
else:
	with open("done.csv","a") as f:
		if t  not in date:
			print(t,file=f)
		print(f"{capitolo} {es}",file=f)


	n = int(es.split(" ")[1])
	if n>=diz[capitolo][f"n_{tipo}"] and  n<diz[capitolo][f"n_{tipo}_max"] :
		print("Si progredisce verso l'infinito :)")
		diz[capitolo][f"n_{tipo}"]+=1 

	with open("es.json","w") as f:
		json.dump(diz,f)


