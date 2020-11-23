import numpy as np
import pandas as pd


path = 'D:\\Data\\task\\01.txt'
path2 = 'D:\\Data\\task\\02.txt'


def openfile(p, x=None):
    with open(p, 'r', encoding='utf-8')as v:
        if x is None:
            lst = []
        for i in v:
            lst.append(i)
    return lst


def table(v2=None):
    oplst = openfile(path)
    oplst2 = openfile(path2)
    if v2 is None:
        lst = []
    for i in oplst:
        lst.append(i)
    for j in oplst2:
        lst.append(j)
    lst = np.unique(lst).tolist()
    return lst


def construction_Token_text1(v2=None):
    c1 = 0
    lst = []
    oplst = openfile(path)
    for i in table():
        for j in oplst:
            if i == j:
                c1 = c1 + 1
                lst.append(c1)
    return lst


def construction_Token_text2(v2=None):
    c1 = 0
    lst = []
    oplst = openfile(path2)
    for i in table():
        for j in oplst:
            if i == j:
                c1 = c1 + 1
                lst.append(c1)
    return lst

vec = construction_Token_text1()
vec2 = construction_Token_text2()

dot = sum(a*b for a,b in zip(vec,vec2))
norm_a = sum(a*a for a in vec) ** 0.5
norm_b = sum(b*b for b in vec2) ** 0.5
cos_sim = dot / (norm_a*norm_b)
print('My version:', cos_sim)
