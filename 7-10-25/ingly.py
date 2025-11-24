word=input("enter a string")
if(word[-3:]=="ing"):
    word=word[:-3]+"ly"
else:
    word=word+"ing"
print(word)
