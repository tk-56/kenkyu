import MeCab
import json
import re
import glob

tagger = MeCab.Tagger("-Owakati")
filename=glob.glob("qiita/*.json")
bodyall=[]
titleall=[]
#wordall=[]

print("jsonの読み込みの開始")
for i in range(len(filename)):
    print(filename[i])
    f=open(filename[i],"r")
    data=json.load(f)
    f.close()
    for k in range(len(data)):
        text=str(data[k]["body"])
        title=str(data[k]["title"])
        text = re.sub(r'https?:\/\/.*?[\r\n ]', '',text)
        text = re.sub('[.]',' ',text)
        text = re.sub('[“]',"",text)
        text = re.sub('[—]',"",text)
        text = re.sub('[\xa0]','',text)
        text = re.sub('[[]','',text)
        text = re.sub('[]]','',text)
        text = re.sub('[(]','',text)
        text = re.sub('[)]','',text)
        text = re.sub('[,]','',text)
        text = re.sub('[”]','',text)
        text = re.sub('[−]','',text)
        text = re.sub('["]','',text)
        text = re.sub('[////]','',text)
        text = re.sub('[0-9]','',text)
        text = re.sub('[:]','',text)
        text = re.sub('[*]','',text)
        text = re.sub('[!-/:-@[-`{-~]','',text)
        text = re.sub(u'[︰-＠]','',text)
        text = re.sub(r'　', ' ', text)  # 全角空白の除去
        text = re.sub('[。]','',text)

        text = tagger.parse(text)
        bodyall.append(text)
        titleall.append(title)

number=[]
for i in range(len(bodyall)):
    if not bodyall[i]:
        number.append(i)
        print("空リストの削除now ")
for i in number:
    del bodyall[i]
    del titleall[i]

print("削除完了")

print("改行文字の削除中")
for i in range(len(bodyall)):
    bodyall[i]=bodyall[i].split()
    while "n" in bodyall[i]: bodyall[i].remove("n")
    while "nn" in bodyall[i]: bodyall[i].remove("nn")
    bodyall[i]=" ".join(bodyall[i])
print("削除完了")

"""
tagger = MeCab.Tagger ("-Ochasen")
for i in range(len(body)):
    tagger.parse("")
    node = tagger.parseToNode(body[i])
    while node:
        if node.feature[0]=="名":
            word.append(node.surface)
        node = node.next
    word=" ".join(word)
    wordall.append(word)
"""

print("ファイルへの書き込み中")
f = open('text/body.txt', 'w')
for i in bodyall:
    f.write(str(i) + "\n")
    #f.write(str(i))
f.close()

f = open('text/title.txt', 'w')
for i in titleall:
    f.write(str(i) + "\n")
    #f.write(str(i))
f.close()

print("システムオールグリーン")
