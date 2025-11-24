number = [3,1,4,9,2,6]
length=len(number)
print("The length of the list iss :",length)
print("The last element of the list is:",number[-1])
print("The items of the list in reverse iss :")
for index in range(length-1,0,-1):
    print(number[index])
if 9 in number:
    print("9 i in the list")
number.insert(7,7)
print(number)
