import pandas as pd
from pandas import Series

# Series
Obj2 = Series([4,7,-5,3],index = ['a','b','c','d'])
print(Obj2)
print('\n')


# Criando uma série sem especificar os índices
Obj = Series([67,78,-56,13])
print(Obj)
print(type(Obj))
print(Obj.values)
print(Obj.index)
print('\n')

# Verifica valores maiores que 3
print([Obj > 3])

#Mostra o valor do index
print(Obj2['b'])

# Verifica se o index existe
print('d' in Obj2)

# Criando uma série de dados passando um dicionário como parâmetro
dicionario = { 'Futebol': 5200, 'Tênis': 120, 'Natação': 698, 'Volleyball': 1550}
Obj3 = Series(dicionario)
print(Obj3)
print(type(Obj3))

# Criando uma lista
esportes = ['Futebol','Tênis','Natação','Basktetball']

# Criando uma série e usando uma lista como índice
Obj4 = Series(dicionario,index=esportes)
print(Obj4)
print("\n")

# Verificando elemento nulo
print(pd.isnull(Obj4))
print("\n")

# Verificando elementos não nulos
print(pd.notnull(Obj4))
print("\n")

# Concatenando Series
Obj3+Obj3
Obj4.name = 'população'
Obj4.index.name = 'esporte'
print(Obj4)






