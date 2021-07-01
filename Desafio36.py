valor = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual é o seu salário?R$ '))
anos= int(input('Em quantos anos vai pagar? '))
prestacao = valor / (anos*12)
prestacaomensal = salario * 30 / 100
if prestacao > prestacaomensal:
    print('Para pagar uma casas de R${:.2f} em {} anos a prestacao será de R${:.2f}. Seu empréstimo NÃO será concedido.'.format(valor, anos, prestacao))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. Seu empréstimo SERÁ CONCEDIDO. PARABÉNS!'.format(valor, anos, prestacao))

