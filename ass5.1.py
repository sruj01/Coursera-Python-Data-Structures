total=0
count=0
while True:
    ival=input('Enter a number: ')
    if ival=='done'or ival=='Done':
        break
    else:
        try:
            fval=float(ival)
            total=total+fval
            count+=1
        except:
            print("Invalid input")
            continue
print('\nTotal: ',total,'\tCount: ',count,'\tAverage: ',total/count)
