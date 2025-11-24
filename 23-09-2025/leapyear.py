current_year=2025
final_year=int(input("enetr the final year"))
for i in range(current_year,final_year):
    if((i%4)==0):
        if((i%100)!=0):
            print(i ,end=",")
        if((i%400)==0):
            print(i,end=",")
