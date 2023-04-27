from datetime import datetime
from random import choice
import json
#cap_es = {1 :33,2 :27, 3:43, 4:27,5 : 0}
with open("es.json","r") as f:
	diz = json.load(f)
#print(diz)

#capitolo = "1"
#print(capitolo)

tipo = choice(["esr","esr","esm"])

t = str(datetime.date(datetime.today()))
with open("done.csv","r") as f:
	lst = f.readlines()
	date = [s.strip() for s in lst if "2023" in s]
	fatti = [s.strip() for s in lst if "2023" not in s]
	fatti_oggi = [s.strip() for s in lst[lst.index(t+'\n')+1::]]

cap_preferiti = ["4"]
lista_possibilita = []
while not lista_possibilita:
	cs = list(diz.keys())+cap_preferiti*10
	capitolo = choice(list(cs))
	lista_possibilita = [f"{tipo} {i}" for i in range(1,1+int(diz[capitolo][f"n_{tipo}"])) if f"{capitolo} {tipo} {i}" not in fatti]*9 #semplicemente i non fatti
	lista_possibilita.extend([lista_possibilita[-1]]*9)
	lista_possibilita.extend([f"{tipo} {i}" for i in range(1,1+int(diz[capitolo][f"n_{tipo}"])) if f"{capitolo} {tipo} {i}" not in fatti_oggi]) #tutti quanti







#print(lista_possibilita)
es = choice(lista_possibilita)
print(f"{capitolo}: {es}")
with open("done.csv","a") as f:
	print(f"{capitolo} {es}",file=f)
	if t  not in date:
		print(t,file=f)


n = int(es.split(" ")[1])
if n>=diz[capitolo][f"n_{tipo}"] and  n<diz[capitolo][f"n_{tipo}_max"] :
	print("Si progredisce verso l'infinito :)")
	diz[capitolo][f"n_{tipo}"]+=1 

with open("es.json","w") as f:
	json.dump(diz,f)



