salary=int(input("Your salary:"))
if salary >=2000:
    tax=salary*0.2
else:
    tax=salary*0.1
net=salary-tax
print("Tax",tax)
print("Net salary:",net)