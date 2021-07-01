from datetime import date
anoAtual = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = anoAtual - nasc
if idade <= 9:
    print('O atleta tem {} anos. Categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {}. Categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos. Categoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos. Categoria: SENIOR'.format(idade))
else:
    print('O atleta tem {} anos. Categoria: MASTER'.format(idade))

