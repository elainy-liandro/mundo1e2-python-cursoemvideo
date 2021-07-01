n = int(input('Digite um número qualquer: '))
par = n % 2
if par == 0:
    print('o número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))