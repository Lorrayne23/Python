# Missão 2: Implementarum algoritmo para determinar se uma string possui todos os caracteres exclusivos.

palavra = input("Digite um palavra : ")

def verificaLetras(palavra): # função que verifica se as letras da palavra digitada se repetem
    salvaLetras = []
    for i in palavra:
        if i not in salvaLetras: # se a letra não estiver na palavra
            salvaLetras.append(i) # adicona a letra , se não , não adiciona

    return len(salvaLetras) # retorna o tamanho da lista de letras verificada

if( verificaLetras(palavra) == len(palavra)): # verifica se o tamanho retornado da lista é compatível com o tamanho da palavra fornecida
    print("A string possui todos os caracteres exclusivos ! ")
else:
    print("A string possui caracteres que se repetem !")

