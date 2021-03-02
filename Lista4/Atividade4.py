lista = [0, 1, 2, 3, 4]

result=list(map(lambda x:[ x**2 , x**3 ] , lista))
for i in result:
     print(i)