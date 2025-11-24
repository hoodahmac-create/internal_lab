names=["hudha","machingal","haroon"]
count=0
for item in names:
    print("count of a in",item,item.count('a'))
    count+=item.count('a')
print("total occurence of a in the list is",count)
