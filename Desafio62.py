print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        while cont <= total:
            print('{} > '.format(termo), end='')
            termo += razao
            cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostra a mais? '))
print('FIM')