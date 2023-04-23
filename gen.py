from random import choice
import json
#cap_es = {1 :33,2 :27, 3:43, 4:27,5 : 0}
f = open("es.json","r")
cap_es= json.load(f)
f.close()


working_caps = ["4","5","6"]
w = open('done.txt','a')
c = choice(list(cap_es.keys()))
n = cap_es[c]
if c in working_caps:
	n+=1
if n!=1:
	n= choice(range(n))+1
print(f"{c} : {n}")
print(f"{c} : {n}",file=w)

if n ==cap_es[c]+1 and c in working_caps:
	cap_es[c] = n
	f = open("es.json","w")
	f.write(str(cap_es).replace("'",'"'))
	f.close()
