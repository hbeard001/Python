def salaryslip(name,salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netsalary=salary-tax
    print("name of employee",name)
    print("salary",salary)
    print("tax",tax)
    print("net salary",netsalary)

salaryslip(input("name"),int(input("salary")))

