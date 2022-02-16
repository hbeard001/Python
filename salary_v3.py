salary=int(input("Your salary:"))
if salary <1000:
    taxRate=0
    if salary >2000:
        taxRate=0.25
    else:
        taxRate =0.15
tax=salary*taxRate
net=salary-tax
print("Tax",tax)
print("Net salary:",net)