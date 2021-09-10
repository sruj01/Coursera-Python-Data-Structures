fn=input('Enter file name: ')
fh=open(fn)
count=0
for l in fh:
    l=l.rstrip()
    if not l.startswith('From '):
        continue
    count+=1    
    w=l.split()
    print(w[1])
print('There were',count,'lines in the file with From as the first word')
