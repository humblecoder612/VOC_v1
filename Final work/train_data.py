
# coding: utf-8

# In[1]:


 #In[2]:


import pandas as pd
xcelmain=pd.ExcelFile("consolidated data.xlsx")


# In[19]:


xcelmain.sheet_names


# In[16]:


sheet_to_df_map = {}
for sheet_name in xcelmain.sheet_names:
    sheet_to_df_map[sheet_name] = xcelmain.parse(sheet_name,header=None)


# In[29]:


sheet_to_df_map["part"].shape


# In[21]:


concater=['part',
 'delay',
 'vehicle',
 'discount',
 'sound',
 'batt',
 'clutch',
 'gear',
 'heat',
 'oil,air,engine,brake,pick',
 'leak',
 'service,serv',
 'delivery',
 'tyre,tyer,tire',
 'KMPL,mileage,KMperL,average',
 'staff',
 'dealer',
 'salesman,sales man,behaviour',
 'sales',
 'response']


# In[23]:


train=pd.concat([sheet_to_df_map[name] for name in concater])


# In[25]:


train.columns=["issue"]


# In[30]:


import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from string import punctuation
from nltk import word_tokenize
STOPWORDS = set(stopwords.words('english'))


# In[32]:


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
    text = text.replace('x', '')
#    text = re.sub(r'\W+', '', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
    return text


# In[38]:


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))
def space_number(text):
    sp=text.split()
    li1=[]
    for word in sp:
        if hasNumbers(word):
            al=list(word)
            li=[]
            for alpha in al:
                if hasNumbers(alpha):
                    string_len=len(alpha)+2
                    alpha=alpha.center(string_len)
                    li.append(alpha)
                else:
                    li.append(alpha)
                newli="".join(li)
            li1.append(newli)
        else:
            li1.append(word)
    ret=" ".join(li1)
    return ret
  


# In[40]:


train["issue"]=train["issue"].apply(clean_text)
train["issue"]=train["issue"].apply(space_number)


# In[41]:


train.to_csv("input2.csv",index=False)

