tot18 = 0
tothomens = 0
totmulheres =0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens +=1
    if sexo == 'F' and idade <20:
        totmulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp =='N':
        break


print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomens} homens cadastrados', end='')
print(f'E temos {totmulheres} mulheres com menos de 20 anos')

