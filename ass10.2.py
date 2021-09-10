fn=input('Enter file name: ')
if len(fn)<1:
     fn='mbox-short.txt'
     fh=open(fn)
else:
    fh=open(fn)
di=dict()
li=list()
li1=list()
for l in fh:
    if l.startswith('From '):
        pos=l.find(':')
        li.append(l[pos-2:pos])
for item in li:
    di[item]=di.get(item,0)+1
for k,v in di.items():
    newtup=(k,v)
    li1.append(newtup)
li1=sorted(li1)   #put li1=sorted(li1,reverse=True) to get descending order
for k,v in li1:
    print(k,v)
