#Missão 3: Implementar um algoritmo para mudar a posição da letra  P do canto superior esquerdo para o canto inferior direito de uma grade

grade = [['|_____|','|_____|','|_____|'],['|_____|','|_____|','|_____|'] ,['|_____|','|_____|','|_____|'],['|_____|','|_____|','|_____|'] ]  # lista para a criação da grade

for i in range(len(grade)):
    for j in range(len(grade[i])):
        if i == 0 and j == 0:
             grade[0][0]='|__P__|'   # grade com a letra P no canto superior esquerdo
        print(grade[i][j], end='')

    print()


print("\n")


for i in range(len(grade)):
    for j in range(len(grade[i])):
        if i == 0 and j == 0:
             grade[0][0]='|_____|'
        if i == 3 and j == 2:
            grade[3][2]='|__P__|' # grade com a letra P no campo inferior direito
        print(grade[i][j], end='')

    print()




