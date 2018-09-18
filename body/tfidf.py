import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
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
gyoretu=X_tfidf.toarray()
gyoretu=gyoretu[NUMBER]
print(title[NUMBER])
for i in range(len(name)):
    if gyoretu[i] > 0:
        print(name[i])
        print(gyoretu[i])
