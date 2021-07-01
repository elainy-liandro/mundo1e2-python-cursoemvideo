from datetime import date
anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
if idade < 17:
    saldo = 18 - idade
    print('Ainda faltam {} para se alistar'.format(saldo))
elif idade == 18:
    print('Já está na hora de se alistar')
elif idade > 18:
    saldo = idade - 18
    print('Já passou {} anos da hora de alistar'.format(saldo))
