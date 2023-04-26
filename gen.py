from random import choice
import json
#cap_es = {1 :33,2 :27, 3:43, 4:27,5 : 0}
with open("es.json","r") as f:
	diz = json.load(f)
#print(diz)

#capitolo = "1"
#print(capitolo)

tipo = choice(["esr","esr","esm"])

with open("done.csv","r") as f:
	fatti = [s.strip() for s in f.readlines()]
#print(fatti)

lista_possibilita = []
while not lista_possibilita:
	capitolo = choice(list(diz.keys()))
	#print(capitolo)
	lista_possibilita = [f"{tipo} {i}" for i in range(1,1+int(diz[capitolo][f"n_{tipo}"])) if f"{capitolo} {tipo} {i}" not in fatti]*5
	lista_possibilita.extend([f"{tipo} {i}" for i in range(1,1+int(diz[capitolo][f"n_{tipo}"]))])
	#print(lista_possibilita)






#print(lista_possibilita)
es = choice(lista_possibilita)
print(f"{capitolo}: {es}")



with open("done.csv","a") as f:
	print(f"{capitolo} {es}",file=f)
n = int(es.split(" ")[1])
if n==diz[capitolo][f"n_{tipo}"] and  n<diz[capitolo][f"n_{tipo}_max"] :
	print("Si progredisce verso l'infinito :)")
	diz[capitolo][f"n_{tipo}"]+=1 

with open("es.json","w") as f:
	json.dump(diz,f)



