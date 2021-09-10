fn=input('Enter file name: ')
fh=open(fn)
for l in fh:
    l=l.rstrip()
    w=l.split()
    if len(w) < 3 :
        continue
    if w[0]!= 'From':
        continue    
    print(w[2])
