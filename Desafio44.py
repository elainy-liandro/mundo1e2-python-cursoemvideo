print('{:=^40}'.format('LOJAS THOP'))
preco = float(input('Preços das compras?R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Escolha uma das opções acima para pagamento: '))
if opcao == 1:
  total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao ==4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas Parcelas?' ))
    parcela = total / totparc
    print('Sua comrpra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
print('Sua compra de R${:.2F} vai custar R${:.2F} no final.'.format(preco, total))


