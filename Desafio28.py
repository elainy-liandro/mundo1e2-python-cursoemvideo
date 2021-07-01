import random

print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
computador = random.randint(0, 5)
jogador = str(input('Em que número pensei? '))
print('PROCESSANDO...')
if jogador == computador:
    print('PARABÉNS!Você conseguiu me vencer!')
else:
    print('GANHEI')


