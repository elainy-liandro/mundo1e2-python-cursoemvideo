'''import random
aluno = input('Quem quer apagar o quadro: ')
escolhido = random.randrange(aluno)
print(escolhido)'''

import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
n5 = str(input('Quinto: '))
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print('O chato é o(a) {} '.format(escolhido))