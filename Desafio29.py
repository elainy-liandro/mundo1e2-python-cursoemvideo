velocidade = int(input('Qual a velocidade atual do seu carro? '))
multa = float((velocidade - 80)*7)
if velocidade >= 81:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. Você deverá pagar uma multa de R${}'. format(multa))
else:
    print('Tenha um bom dia!')

