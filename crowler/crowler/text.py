import json


bodyall=[]
f=open("result.json","r")
data=json.load(f)
f.close()
text=data[8]["code"]

print(text)

f = open('text.txt', 'w')
for i in text:
    f.write(str(i))
    #f.write(str(i))
f.close()
