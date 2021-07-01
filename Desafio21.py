import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('O Segundo aluno: '))
n3 = str(input('O terceiro aluno: '))
n4 = str(input('O quarto aluno: '))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será{}'.format(lista))