#not
print(not(True))

name=""
if not name:
    print("Name is empty")

value= True
if value:
    print(value)
else:
    print(not value)

#nested if-else
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1==0 or num2==0:
        print("num1 or num2 is zero")
else:
    if num1>num2:
        print("num1 is greater")
    else:
        print("num2 is greater")
