distancia = float(input('Qual é a distância da sua viagem? '))
print('VocÊ esta prestes a iniciar uma viagem de {}'.format(distancia))
if distancia <= 200:
      preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('Sua viagem custará R${:.2f}'.format(preco))





