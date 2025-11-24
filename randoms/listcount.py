text="hello hi welcome to hi hi hello welcome"
textt=text.split()
print("count of hello",textt.count('hello'))
print("count of hi",textt.count('hi'))
print("count of welcome",textt.count('welcome'))
print("count of to",textt.count('to'))

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
