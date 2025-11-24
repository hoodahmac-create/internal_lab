n=int(input("hoe many words?"))
words=[]
for i in range(0,n):
    word=input("enter a word")
    words.append(word)
larger=""
for i in range(0,len(words)):
    if len(words[i])>len(larger):
        larger=words[i]
print("length of the largest word,",larger,"is",len(larger))
