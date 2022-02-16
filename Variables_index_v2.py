nums=[]
choice="y"
while choice=="y"or choice=="Y":
    no=int(input("Enter any number"))
    nums.append(no)
    choice=input("....Do you want to add another?")

print("you have entered",len(nums),"values")
print(nums)
