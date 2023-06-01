import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Embeddings file 
embeddingsIndex = {}

f = open(os.path.join(r"D:\Embeddings\Embeddings_2020-01-23\Embeddings_2020-01-23\Embeddings_ES\Scielo_Wikipedia\Word2Vec\300\W2V_scielo_wiki_w10_c5_300_15epoch.txt"),  encoding='utf8')
f.readline()
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddingsIndex[word]= coefs
f.close()


def get_embedding(word):
    emb = embeddingsIndex.get(word, 0)
    return emb

#print(len(embeddingsIndex.get(word, 0)))