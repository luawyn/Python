for i in range(1, 6, 1):  # começa no 1, vai até 6, de 1 em 1
    print(i)

    soma = 0
    qtd = 0
    for i in range(1, 101):
        if (i % 2 == 0):
            soma += i
            qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}'.format(media))

for tabuada in range(1, 11, 1):
    print('Tabuada do {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
