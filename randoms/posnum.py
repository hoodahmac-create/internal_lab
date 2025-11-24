listt=[25,1,-3,4,-2,30]
for num in listt:
    if num>0:
        print(num, end=",")
        
sumn=0
print("\n")
for n in range(1,11):
    sumn+=n
print("sum of the first ten natural numbers is:",sumn)

fact=1
number=int(input("enter a number"))
for i in range(number,1,-1):
    fact*=i
print("The factorial of",number,"is:",fact)
