import pandas as pd
import numpy as np
from pandas import DataFrame
import sys

# Usando o método read_csv
df = pd.read_csv('salarios.csv')

# Usando o método read_table
df = pd.read_table('salarios.csv', sep=',')

# Alterando o título das colunas
df = pd.read_csv('salarios.csv', names = ['a','b','c','d'])

data = pd.read_csv('salarios.csv')
data.to_csv(sys.stdout, sep='|')

# Criando um Dataframe
dates = pd.date_range('20180101', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
print(df.head())
print("\n")

# Quick data summary
print(df.describe())
print("\n")

# Calculando a média / por coluna
print(df.mean())
print("\n")

# Pivot e cálculo da média / por linha
print(df.mean(1))
print("\n")

# Usando métodos
print(df.apply(np.cumsum))
print("\n")

# Merge de Dataframes
left = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna1': [1, 2]})
right = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna2': [4, 5]})
print(pd.merge(left, right, on='chave'))
print("\n")

# Adicionando um elemento ao Dataframe
df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
print(df)
print("\n")

# Adicionando um elemento ao Dataframe
s = df.iloc[3]
df.append(s, ignore_index=True)
print(df)
