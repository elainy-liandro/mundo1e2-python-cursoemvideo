primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input(' Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiroValor + segundoValor
        print('A soma entre {} + {} é {}'.format(primeiroValor, segundoValor, soma))
    elif opcao == 2:
        multiplicar = primeiroValor * segundoValor
        print('A multiplicação entre {} x {} é {}'.format(primeiroValor, segundoValor, multiplicar))
    elif opcao == 3:
        if primeiroValor > segundoValor:
            print('O primeiro valor {} é maior que o segundo valor {}'.format(primeiroValor, segundoValor))
        elif segundoValor > primeiroValor:
            print('O segundo valor {} é maior que o primeiro valor {}'.format(segundoValor, primeiroValor))
        else:
            print('o dois valores informados {} e {} são iguais'.format(primeiroValor, segundoValor))
    elif opcao ==4:
        print('Informe os números novamente: ')
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opçao inválida. Tente novamente!')

print('Fim do programa! Volte sempre!')