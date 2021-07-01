soma = 0
continuar = 'S'
medio = 0
quant = 0
maior = 0
menor = 0
while continuar in 'Ss':
    n1 = int(input('Digite um número: '))
    soma += n1
    quant += 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / quant
print('Você digitou {} números e a média foi {:.2f}.'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))