from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from sklearn.preprocessing import normalize
import re 
import numpy as np
from getEmbeddings import get_embedding

#if the embeddings were trained on non-lemmatized text, introducing lemmatization may result in a mismatch between the vocabulary used in the embeddings and the vocabulary in the processed documents
#in this case the embeddings were trained on non lemmatized text 

stopWords = stopwords.words("spanish")

def procesarText(text):
    lower = text.lower()
    x= re.sub(r'^RT[\s]+', '', lower)
    x= re.sub(r'https?://[^\s\n\r]+', '', x)
    x= re.sub(r'#','', x)
    x= re.sub("[^a-zA-Z0-9]", " ", x)
    x = word_tokenize(x)
    x = [word for word in x if word not in stopWords]

    emb = np.zeros((300,))
    for word in x:
        emb += get_embedding(word)
        emb/len(x)
    emb = normalize([emb], norm='l2')[0]  #normalize L2 sklearn    
    return emb


    