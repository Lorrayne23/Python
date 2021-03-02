import numpy as np
import matplotlib
import matplotlib.pyplot as plt



# Criando array a partir de lista
vetor1 = np.array([0,1,2,3,4,5,6,7,8])
print(vetor1)

# cumsum retorná soma cumulativa
print(vetor1.cumsum())

# Imprimindo na tela um elemento específico
print(vetor1[2])

# Alterando um elemento :
vetor1[2]=3 # não é possível incluir elemento de outro tipo
print(vetor1)

# Verificando o formato
print(vetor1.shape)

# Função range cria um vetor contendo uma progressão aritmética a partir de um intervalo - start,stop,step
vetor2 = np.arange (0,4,0.25)
print(vetor2)

# Verificando o tipo
print(vetor2.dtype)

# Array de 10 posições com valores 0's
print(np.zeros(10))

# Retorna 1 nas posições em diagonal e 0 no restante
z = np.eye(4)
print(z)

# Valores passados como parâmetro , formam uma diagonal
d = np.diag(np.array([1,2,3,4]))
print(d)

# O método linspace (linearly spaced vector) retorna um número de
# valores igualmente distribuídos no intervalo especificado
e = np.linspace(0,10)
print(e)


# Criando uma matriz
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)

print(matriz.shape)

# Criando matriz 2 x # apenas com números "1"
matriz1 = np.ones((2,3))
print(matriz1)

# Criando uma matriz a partir de uma lista de listas
lista = [[12,81,22],[0,34,59],[21,48,94]]
matriz2 = np.matrix(lista)
print(matriz2)
print(type(matriz2))

# Tamanho da matriz
print(matriz2.size)

# Elemento da matriz
print(matriz2[2,1])

# Alterando um elemento da matriz
matriz2[0,1] = 100
print(matriz2)

x = np.array([1, 2])  # NumPy decide o tipo dos dados
y = np.array([1.0, 2.0])  # NumPy decide o tipo dos dados
z = np.array([1, 2], dtype=np.float64)  # Forçamos um tipo de dado em particular

print(x.dtype,y.dtype,z.dtype)

matriz3 = np.array([[24,36],[88,94]],dtype=float)
print(matriz3)

# Usando o método random() do Numpy
plt.hist(np.random.rand(1000))
plt.show()

print(np.random.rand(10))

# Random com 5 linhas e 5 ccolunas

print(np.random.randn(5,5))

# Estatística

# Criando um array
A = np.array([15,23,63,94,75])

# Média
print(np.mean(A))

# Desvio padrão
print(np.std(A))

# Variância
print(np.var)

# Soma
d = np.arange(1,10)
print(np.sum(d))

# Produto
print(np.prod(d))

# Slicing
a = np.diag(np.arange(3))
b = np.arange(10)
print(a)
print(b)

print(b[2:9:2])

# Comparação
n = np.array([1,2,3,4])
m = np.array([4,2,2,4])
print(np.array_equal(a,b))

# menor valor
print(n.min())

# maior valor
print(n.max())

# Somando um elemento ao array
print(np.array([1,2,3])+1.5)

# Usando o método around
a = np.array([1.2,1.5,1.6,2.5,3.5,4.5])
b = np.around(a)
print(b)

# Copiando um array
B = np.array([1,2,3,4])
print(B)
C = B.flatten()
print(C)

# Repetindo os elementos de array
v = np.array([1,2,3])
print(np.repeat(v,3)) # repete 1 elemento a quantidade de vezes informadas
print(np.tile(v,3)) # repete o cojunto de elementos a quantidade de vezes informada

# Concatenando array
w = np.array([5,6])
print(np.concatenate((v,w),axis=0))

# Outro modo de copiar arrays
r = np.copy(v)
print(r)











