import collections

newwordlist=[]
f = open('count/tfcount.txt', 'r',encoding="utf-8")
wordlist = f.readlines()
f.close()
for i in range(len(wordlist)):
    text = wordlist[i].replace('\n','')
    newwordlist.append(text)

d = collections.Counter(newwordlist)


print(d.most_common(10))
