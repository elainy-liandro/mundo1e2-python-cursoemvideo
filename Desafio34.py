sal = float(input('Qual o valor do seu salário? '))
if sal <= 1250:
    aumento = (sal + (sal*15/100))
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora.'.format(sal, aumento))
else:
    aumento2 = (sal + (sal*10/100))
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora'.format(sal, aumento2))

