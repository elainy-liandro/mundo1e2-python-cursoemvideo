soma = 0
n1 = 0
cont = 0
n1 = int(input('Digite um valor [999 para parar]: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Digite um valor [999 para parar]: '))

print('A soma entre os números digitados foram {}'.format(soma))


