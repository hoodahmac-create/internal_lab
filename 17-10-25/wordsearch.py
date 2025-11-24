sentence=input("enter a sentence")
words=sentence.split()
count=0
flag=0
key=input("enter the word you want to search")
for i in range(0,len(words)):
    count+=1
    if words[i]==key:
        print("The word",key,"is the",i+1,"th word in the sentence")
        flag=1
        break
if flag!=1:
    print("The word is not in the sentence")
