#!/usr/bin/env python
# coding: utf-8
primeira vez em jupyter e mineconda
# In[1]:


# revisão
nome = 'joaquim'
idade = 34
valor_em_carteira = 345.99
vip = True # false
nome = 99 + 1
print(nome)


# In[2]:


def soma_de_valores(valor1, valor2):
    resultado = valor1 + valor2
    return resultado


valor1 = 20
valor2 = 18

soma = soma_de_valores(valor1, valor2)
print(soma)


# In[3]:


lista_de_clientes = ["pedro", "pablo", "solange", "alvarez"]
lista_de_itens = ["banana", "mala", "carro", "sirene"]
print(lista_de_clientes)

lista_de_clientes.append("julia")

print(lista_de_clientes)
lista_de_clientes[4]


# In[27]:


#tupla
lista_de_vendas=[]
venda = ("banana",4,8.0)
lista_de_vendas.append(venda)
print(lista_de_vendas)


# In[40]:


cliente1 ={
    "nome": "pedro",
    "idade": 23,
    "vip": True,
    "carteira":10000000000000000000000,
}

cliente2 ={
    "nome":"lagie",
    "idade":32,
    "vip": False,
    "carteira":200000000000,
}

cliente1 ["idade"] = 25
lista_de_clientes = (cliente1,cliente2)
print(cliente1["carteira"])


# In[48]:


import math
print(math.sqrt(4))


# In[ ]:




