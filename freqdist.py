
# coding: utf-8

# In[1]:

import nltk


# In[2]:

from nltk.corpus import stopwords
stopwords.words('english')


# In[3]:

for i in range(5):
    a = open("E:/IE_Project/output2/output_reviews_books_com_split_1/output_reviews_books_com_%s.txt" %(i + 1)).read()


# In[4]:

tokens = nltk.word_tokenize(a)


# In[ ]:

from nltk import FreqDist


# In[25]:

a = open("E:/IE_Project/output2/output_reviews_books_com_split_1/output_reviews_books_com_1.txt").read()
stopwords = nltk.corpus.stopwords.words('english')
content = [w for w in tokens if w.lower() not in stopwords]
fdist1 = FreqDist(content)


# In[26]:

import sys


# In[29]:

fdist1
sys.stdout = open('E:/IE_Project/output2/output_reviews_books_com_split_1/output_reviews_books_result.txt', 'w')


# In[11]:

with open('E:/IE_Project/output2/output_reviews_books_com_split_1/output_reviews_books_result.txt', 'w') as f:
    f.writelines(fdist1)


# In[20]:

import pickle
pickle.dump(fdist1, open( "E:/IE_Project/output2/output_reviews_books_com_split_1/output_reviews_books_result.txt", "wb" ) )


# In[ ]:



