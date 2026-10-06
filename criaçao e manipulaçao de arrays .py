#!/usr/bin/env python
# coding: utf-8

# In[ ]:


aula2:modulo1


# In[5]:


#criar sequencia python
python_list = [i for i in range(1_000_000 + 1)]

##tempo de execuçao: 0.107s
##memóris utilizada:39.8 mib


# In[6]:


import numpy as np


# In[7]:


#criar sequencia numpy
numpy_array = np.arange(0, 1_000_000 + 1, dtype='int64')
## Tempo de execução: 0.008 s
## Memória utilizada: 7.5 MIB


# In[8]:


#calcular quadrados python

python_list_square = [i**2 for i in python_list]

##tempo de execução:0.520s
##Memoria utilizada: 38.4 MiB


# In[9]:


#calcular quadrados numpy
numpy_array_square = numpy_array**2
##Tempo de execução:0.005s
##Memoria utilizada:7.5 MIB


# ## Tipo e acesso aos Elementos de um Array

# In[10]:


#criando um Array
arr = np.array([1, 2, 3, 4, 5])
print(f"Elementos: {arr}, Tipo dos elementos: {arr.dtype}, Tamanho do array: {arr.shape}")


# In[11]:


#acesso ao terceiro do array(indice 2):
Elementos = arr[2]
print(Elementos)


# In[12]:


#obtendo elementos de indice 1 a 3
subset = arr[1:4]
print(subset)


# In[13]:


#criando uma matriz
matrix  = np.arange(1., 10.).reshape((3, 3))
print(matrix)
print(f"Tipo dos elementos: {matrix.dtype}, Dimensões da matriz: {matrix.shape}")


# In[14]:


## acessando a 3 linha:
linha = matrix [2]
print(linha)


# In[15]:


## acessando a 2 coluna:
coluna = matrix[:, 1]
print(coluna)


# In[16]:


a = np.array([1.0, 2.0, 3.0])
b=2.0

Resultado = a * b
print(Resultado)


# ## Multiplicação de Matrizes

# In[22]:


A = np.array([[1,2], [3,4], [5,6]])
B = np.array([[1], [2]])
print(A)


# In[18]:


print(B)


# In[24]:


## Multiplicaçao utilizando apenas listas python
C = [[0], [0], [0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
         C[i][j] += A[i][k] * B[k][j]
print(C)


# In[25]:


##agora vamos realizar a mesma operaçao com Numpy]
D = A @ B
print(D)


# In[26]:


N = 500

A = np.arange(N*N, dtype='int64').reshape(N,N)
B = A * 2

C = A @ B
print(C)

##tempo de execuçao:0.196s
##Memoria utilizada: 5.8 MIb


# In[27]:


A_lst = A.tolist()
B_lst = B.tolist()
C_lst = np.zeros_like(A).tolist()

for i in range(len(A_lst)):
    for k in range(len(B_lst)):
        C_lst[i][j] += A_lst[i][k] * B_lst [k][j]
print(C)
##Tempo de execuçao: 66.462s
##Memoria utilizada: 211.6 MiB


# In[ ]:




