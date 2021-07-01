print('-='*20)
print('\33[4;31;46mAnalisador de Triângulos\033[m')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR Triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo')