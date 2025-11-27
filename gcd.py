n=int(input("enter a numb"))
n1=int(input("enter a numb"))
gcd=1
if(n<n1):
    smaller=n
else:
    smaller=n1
for i in range(1,smaller+1):
    if(n%i==0 and n1%i==0):
        gcd=i
print(gcd)