listaA = [2, 3, 4]
listaB = [10, 11, 12]
listasElevadas = list(map(lambda x,y : x**y , listaA,listaB))

for i in listasElevadas:
    print("O valor de um elemento de listaA elevado a outro elemento de listaB é :",i)