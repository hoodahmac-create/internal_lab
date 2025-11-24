n=int(input("enter the value for n"))
def pyr(n):
    for i in range(1,n+1):
        m=i
        for j in range(i):
            print(m,end=" ")
            m+=i
        print("\n")
pyr(n)
