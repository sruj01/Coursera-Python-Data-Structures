largest=None
smallest=None
while True:
    val=input('Enter a number: ')
    if val=='Done' or val=='done':
        break
    else:
        try:
            ival=float(val)
            if largest==None or smallest==None:
                largest=ival
                smallest=ival
            elif ival < smallest:
                smallest=ival
            elif ival > largest:
                largest=ival
        except:
            print('Invalid input')
            continue
print('\nMaximum is',largest,'\nMinimumm is',smallest)
