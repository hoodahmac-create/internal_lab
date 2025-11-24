def input_Number():
    while(True):
        n=int(input("enter a number greater than or equal to 1000"))
        if n<=1000:
            print("The number entered should contain minimum 4 digits. Try again!")
            continue
        else:
            break
    return n
def reverse_Number(n):
    length=len(str(n))
    rev=0
    for i in range(length):
        mod=n%10
        n=n//10
        rev=(rev*10)+mod
    return rev
number=input_Number()
reverse=reverse_Number(number)
print(number,reverse)
