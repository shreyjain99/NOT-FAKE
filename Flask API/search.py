#%%
from gensim import models
import numpy as np
import pandas as pd
from scipy import spatial
import pandas as pd
from sklearn.neighbors import KDTree
#%%
# wv = models.KeyedVectors.load_word2vec_format("./w2v/word2vec-google-news-300.gz", binary=True)
#%%
class Similar():
    def __init__(self, data_path: str = "C:/Users/Admin/BE PROJECT/search_covid.pkl", wv=None):
        self.data = pd.read_pickle(data_path)
        self.wv = wv
        if(self.wv == None): self.wv = models.KeyedVectors.load_word2vec_format("C:/Users/Admin/gensim-data/word2vec-google-news-300/word2vec-google-news-300.gz", binary=True)
        self.tree = KDTree(self.data["w2v"], leaf_size=2)

    def _make_w2v(self, sentence):
        vector = [0 for i in range(300)]
        added = 0
        if(type(sentence) == float): sentence = str(sentence)
        for word in sentence.split(" "):
            if len(word) < 2: continue
            if word not in self.wv.key_to_index: continue
            else:
                vector = vector + self.wv[word]
                added+=1
        if(added != 0): vector = [e/added for e in vector]
        return vector

    def _top_k_similar(self, sentence):
        sentence_w2v = self._make_w2v(sentence=sentence)
        distance, idx = self.tree.query(sentence_w2v,k=20)
        top_news = [self.data["text"][x] for x in idx]
        return top_news
    
    def pred(self, content: str):
        top_news = self._top_k_similar(content)
        return top_news
# %%
# model = Similar(wv=wv)
# %%
#pred = model.pred("Hello World")