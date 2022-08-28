mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)  # altera os dados normalmente, diferente da Tupla.

mochila.append('Ovos')  # acrescenta no final da lista *apendice
print('Lista: ', mochila)

# acrescenta no índice que você escolher e desloca o resto
mochila.insert(1, 'Canivete')
print('Lista: ', mochila)

del mochila[1]  # deleta o índice 1
print('Lista: ', mochila)

mochila.remove('Ovos')  # deleta ovos não importando o local que ele está
print('Lista: ', mochila)

# cópia
x = [5, 7, 9, 11]
y = x[:]
print(x)
print(y)

# lista dentro de lista:

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item:'))
    item.append(int(input('Digite a quantidade:')))
    item.append(float(input('Digite o valor:')))
    mercado.append(item[:])
    item.clear()
print(mercado)

soma = 0
print('Lista de compras:')
print('-' * 20)
print('Item | Quantidade | Valor unitário | Total do item')
for item in mercado:
    print('{} | {} | {} | {}'.format(
        item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))
