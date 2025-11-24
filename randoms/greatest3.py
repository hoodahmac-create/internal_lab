num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
num3=int(input("enter your third number"))
if num1>=num2 and num1>=num3:
     print(num1,"is the greatest out of the three numbers")
elif num2>=num3:
    print(num2,"is the greatest out of the three numbers")
else:
     print(num3,"is the greatest out of the three numbers")
