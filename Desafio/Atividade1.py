# Missão 2: Gerar uma lista de números primos.

listaValor = [i for i in range(1,100)] # adicona números de 1 a 99 a lista


def primos(listaValor): # função que verifica se o número é primo
    listaPrimo=[]
    for i in listaValor:
        soma = 0
        for j in range(1, i + 1):
            if i % j == 0: # se o número for divísivel por j adiciona-se ele a variável soma
                soma += 1

        if soma == 2 : # se a soma for igual a 2
          listaPrimo.append(i)  # adiciona o número na lista de primos

    return listaPrimo


print(primos(listaValor))













