bill=int(input("Enter your bill: "))
paid=int(input("enter amount paid: "))
x=paid-bill
if int(x/10)>=1:
    a=int(x/10)
    print("£10: ",a)
    x=x-(10*a)
if x>=5:
    print("£5: ",1)
    x=x-5
if int(x/2)>=1:
    c=int(x/2)
    print("£2: ",c)
    x=x-(2*c)
if  x=1:
    print("£1: ",1)
    x=x-1
    
