fn=input('Enter file name: ')
fh=open(fn)
count=0
total=0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count+=1
        num = float(line[21:])
        total = num + total
print('Average spam confidence: ',total/count)
