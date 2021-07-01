n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) /2
if m >= 7.0:
    print('PARABÉNS! Você tirou média {} e foi APROVADO!'.format(m))
elif m > 5:
    print('Estude mais, você ficou de RECUPERAÇÃO')
elif m < 4.9:
    print('REPROVADO')