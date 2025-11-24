word=input("enter a string")
words=word[0]
for i in range(1,len(word)):
    if word[i]!=word[0]:
        words+=word[i]
    else:
        words+="$"
print(words)
