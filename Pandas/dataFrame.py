import pandas as pd
from pandas import DataFrame
import numpy as np

# DataFrame
data = {'Estado': ['Santa Catarina', 'Paraná','Goiás','Bahia','Minas Gerais'],
        'Ano': [2002,2003,2004,2005,2006],
        'População':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
print(frame)
print('\n')
print(type(frame))

# Adicionando nomeação de colunas
DataFrame(data,columns=['Ano','Estado','População'])
print(DataFrame)
print("\n")

# Criando outro dataframe com os mesmos dados anteriores mas adicioando uma coluna
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'],
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])
print(frame2)
print("\n")

# Imprimindo apenas uma coluna do DataFrame
print(frame2['Estado'])
print("\n")

print(frame2.index )
print("\n")

print(frame2.columns)
print("\n")


print(frame2.values)
print("\n")

print(frame2.dtypes)
print("\n")

print(frame2.Ano)
print("\n")

print(frame2[:2])
print("\n")

# Usando Numpy e Pandas

# Usando o Numpy para alimentar uma das colunas do dataframe
frame2['Débito'] = np.arange(5.)
print(frame2)
print("\n")

# Resumo da Dataframe
print(frame2.describe())
print("\n")

# Mostra dataframe de tal valor a outro
print(frame2['dois':'quatro'])
print("\n")

# Mostra os valores menores que 2 em população
print(frame2[frame2['População'] < 2])
print("\n")

# Localizando registros dentro do dataframe
print(frame2.loc['quatro']) # mostra valores em 'quatro'
print("\n")

print(frame2.iloc[2]) # mostra valores do índice 2
print("\n")

# Inveretnedo as colunas e índices
# Criando um dicionário
web_stats = {'Dias': [1,2,3,4,5,6,7],
             'Visitantes': [45,23,67,78,23,12,14],
              'Taxas':[11,22,33,44,55,66,77]}

df = pd.DataFrame(web_stats)
print(df)
print("\n")

# Vizualizando uma coluna como index
print(df.set_index('Dias'))
print("\n")

print(df.head())
print("\n")

print(df['Visitantes'])
print("\n")

print(df[['Visitantes','Taxas']])








