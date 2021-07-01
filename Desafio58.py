import random
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
        jogador = int(input('Qual é o seu palpite? '))
        palpite += 1
        if jogador == computador:
            acertou = True
        else:
                if computador > jogador:
                        print('Mais... Tente mais uma vez.')
                elif computador < jogador:
                        print('Menos... Tente mais uma vez')
print('PARABÉNS você acertou na {}ª tentativa'.format(palpite))


