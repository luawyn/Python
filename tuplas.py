mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0])  # Elemento 1 - índice 0
print(mochila[2])  # Elemento 3 - índice 2
print(mochila[0:2])  # Elementos 1 e 2 - índice 0 e 1
print(mochila[2:])  # Elementos a partir do índice 2
print(mochila[-1])  # Último elemento

# Não pode fazer atribuição em Tuplas, são imutáveis

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

# Desempacotamento de parâmetros em funções


def soma(*num):
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma


print('Resultado: {}\n'.format(soma(1, 2)))
print('Resultado: {}\n'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9)))
