hours=int(input('Enter hours: '))
rate=float(input('Enter rate: '))
pay=hours*rate
if hours<=40:
    print(pay)
elif hours>40:
    pay=(40*rate)+((hours-40)*rate*1.5)
    print(pay)
