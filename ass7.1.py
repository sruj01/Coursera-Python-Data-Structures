fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
    print('Bad file name: ',fname)
    quit()
for line in fhandle:
    print(line.rstrip().upper())   #can use the functions in any order i.e line.upper().rstrip() is also valid
