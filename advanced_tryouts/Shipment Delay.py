
# coding: utf-8

# In[35]:

a = open("C:/Users/saiad/Desktop/IE Project/reviews_Electronics_split_9/reviews_Electronics_3.txt").read()


# In[2]:

import re
import nltk


# In[36]:

sents = nltk.sent_tokenize(a)


# In[37]:

mystring = ("feature", "delivered late", "delayed", "Shipment delayed","arrived early","late delivered",
             )
text = str()
for line in sents:
    if any(x in line for x in mystring):
    #if mystring in line:
          text = text + line


# In[38]:

with open('C:/Users/saiad/Desktop/IE Project/Output/reviews_Electronics_3.txt', 'w') as f:
    f.writelines(text)


# In[ ]:

a = open("C:/Users/saiad/Desktop/IE Project/reviews_Electronics_split_9/reviews_Electronics_3.txt").read()

