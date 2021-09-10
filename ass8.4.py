lst=list()
fn=input('Enter file name: ')
fh=open(fn)
for l in fh:
    for w in l.split():
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)
