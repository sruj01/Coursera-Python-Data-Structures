fname=input("enter file name: ")
fhandle=open(fname)
counts=dict()
list=list()
bigv=None
bigk=None
for l in fhandle:
    if l.startswith('From '):
        w=l.split()
        list.append(w[1])
for item in list:
    counts[item]=counts.get(item,0)+1
for k,v in counts.items():
    if bigv == None or v>bigv:
        bigk=k
        bigv=v
print(bigk,bigv)
