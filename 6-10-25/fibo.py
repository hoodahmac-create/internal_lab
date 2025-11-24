n=int(input("enetr the limit"))
def fib(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fib(n)
