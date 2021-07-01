
while True:
    print('-' * 20)
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    if tabu < 0:
        break
    print('-' * 20)
    for c in range(0, 11):
        multi = tabu * c
        print(f'{tabu} x {c} = {multi}')
print('Tabuada encerrada. Volte sempre!')