nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em Maiusculo é {}'.format(nome.upper()))
print('Seu nome em Minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



