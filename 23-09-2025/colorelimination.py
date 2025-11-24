list1=["red","green","black","purple"]
list2=["purple","green","white","brown"]
for i in list1:
    if i not in list2:
        print(i,end=",")
