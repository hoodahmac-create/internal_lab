
l=[]
n=int(input("eneter the size of the lsit"))
for i in range(0,n):
    num=int(input("enetr your numbr"))
    if num>100:
        l.append("over")
    else:
        l.append(num)
    i+=1
print(l)
