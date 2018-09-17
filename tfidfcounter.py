import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import heapq
np.set_printoptions(threshold=np.inf)

NUMBER=56 #表示したい記事番号


f = open('text/body.txt', 'r',encoding="utf-8")
body = f.readlines()
f.close()

f = open('text/title.txt', 'r',encoding="utf-8")
title = f.readlines()
f.close()

tfidf_vect = TfidfVectorizer()
X_tfidf = tfidf_vect.fit_transform(body)
name=tfidf_vect.get_feature_names()
gyoretuall=X_tfidf.toarray()


"""
gyoretu=gyoretu[NUMBER]
print(title[NUMBER])
for i in range(len(name)):
    if gyoretu[i] > 0:
        print(name[i])
        print(gyoretu[i])
"""
dicall={}
wordlist=[]
counter=0
for i in range(len(gyoretuall)):
    gyoretu=gyoretuall[i]
    for s in range(len(gyoretu)):
            if gyoretu[s] > 0:
                dic={name[s]:gyoretu[s]}
                dicall.update(dic)
                counter+=1
    if counter > 10:
        sorted_dicall=sorted(dicall.items(), key=lambda x: -x[1])
        for k in range(10):
            wordlist.append(sorted_dicall[k][0])
    dicall={}
    counter=0
print(wordlist)

f = open('count/tfcount.txt', 'w',encoding="utf-8")
for i in wordlist:
    f.write(str(i)+"\n")
f.close()
