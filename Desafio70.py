print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
totPreco = 0
quantproduto = 0
acima =0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    totPreco += preco
    if preco > 1000:
        acima += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break
print(f'O total de compra foi R${totPreco}')
print(f'Temos {acima} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')