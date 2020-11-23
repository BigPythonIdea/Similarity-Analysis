import numpy as np
import pandas as pd
import re
from tensorflow.keras.preprocessing.text import Tokenizer

path = 'D:\\Data\\task\\01.txt'
path2 = 'D:\\Data\\task\\02.txt'
lst = []
toklst = []


def openfile(p):
    with open(p, 'r', encoding='utf-8')as v:
        for i in v:
            lst.append(i)


def tok(v, v2=None):
    if v2 is None:
        lst = []
    for i in v:
        lst.append(i)
    lst = np.array(lst)
    tok = Tokenizer()
    tok.fit_on_texts(lst)
    txs = tok.texts_to_sequences(lst)
    txs = list(filter(None, txs))
    txs = np.array(txs)
    for i in txs:
        for j in i:
            toklst.append(j)
    return toklst


openfile(path)
vec = tok(lst)

openfile(path2)
vec2 = tok(lst)

from sklearn.metrics.pairwise import cosine_similarity

dot = sum(a * b for a, b in zip(vec, vec2))
norm_a = sum(a * a for a in vec) ** 0.5
norm_b = sum(b * b for b in vec2) ** 0.5
cos_sim = dot / (norm_a * norm_b)
print('My version:', cos_sim)
# print('Scikit-Learn:', cosine_similarity([vec], [vec2]))