#!/usr/bin/env python
# coding: utf-8

# In[7]:


#pip3 install pandas


# In[8]:


import pandas as pd 


# ### Series

# In[34]:


cidades =[
    "Sao paulo (SP)",
    "Rio de Janeiro (RJ)",
    "Brasilia (DF)",
    "Fortaleza (CE)",
    "Salvador (BA)",
    "Belo Horizonte (MG)",
    "Manaus (AM)",
    "Curitiba (PR)",
]

populaçao = [
    12,
    6.5,
    3,
    2.4,
    2.3,
    2,
    1.7

]

cidades_serie = pd.Series(cidades)
cidades_serie

populaçao_serie = pd. Series(populaçao)
populaçao_serie

cidades_serie[3]
cidades_serie[3:6]
populaçao_serie.max()
populaçao_serie.mean()
populaçao_serie * 2




# ### DataFrames

# In[106]:


cidades_populosas = pd.DataFrame ({'cidade' : cidades_serie, 'populaçao em milhoes': populaçao_serie})
cidades_populosas



# In[107]:


cidades_populosas.info()


# In[108]:


cidades_populosas ['cidade']


# In[109]:


cidades_populosas.iloc[3]


# In[110]:


cidades_populosas.iloc[3:7]


# In[111]:


cidades_populosas.head()


# In[112]:


cidades_populosas.tail()


# In[113]:


cidades_populosas ['populaçao em milhoes'].mean()


# #### Adicionando colunas
# 

# In[114]:


Area_urbana =[
    '914',
    '740',
    '520',
    '620',
    '240',
    '856',
    '145',
    '123',
]


# In[115]:


cidades_populosas ['Area urbana em km²'] = area_urbana
cidades_populosas


# ### Aplicando Funções
# 

# In[116]:


cidades_populosas['populaçao'] = cidades_populosas['populaçao em milhoes'] * 1_000_000
cidades_populosas


# In[117]:


cidades_populosas.info()


# In[119]:


cidades_populosas['Area urbana em km²'] = cidades_populosas['Area urbana em km²'].astype(int)
cidades_populosas.info()


# ### Combinando dados de colunas

# In[121]:


cidades_populosas['habitantes por km²'] = cidades_populosas['populaçao'] / cidades_populosas['Area urbana em km²']
cidades_populosas


# In[ ]:




