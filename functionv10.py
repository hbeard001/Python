def tax(salary):
    t=salary*0.2
    return t


salary=int(input("Please enter your salary: "))
net_salary=salary-tax(salary)
print("Tax",tax(salary))
print("net",net_salary)
