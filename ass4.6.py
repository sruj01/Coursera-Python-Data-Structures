hours=int(input("Enter hours: "))
rate=float(input("Enter rate: "))
def computepay(r,h):
    pay=r*h
    if r>0:
        if h<=40 and h>0:
            return pay
        elif h>40:
            pay=(40*r)+(h-40)*rate*1.5
            return pay
        else:
            return print("Error: Hour cannot be negative")
    else:
        print("Error: Rate cannot be 0 or negative")
print("Pay",computepay(rate,hours))
