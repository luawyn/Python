a = 1
b = 5
resposta = a == b  # a é diferente de b, false
print(resposta)
resposta = a != b  # a é diferente de b, true
print(resposta)

nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'
print(nota)
print(disciplina)

texto = 'Você tirou %.1f na disciplina de Algoritmos' % nota
print(texto)
# %d numeros inteiros, %f numeros de ponto flutuante, %s strings
texto = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(texto)

# também pode ser feito usando format, mais indicado
texto = 'Você tirou {} na disciplina de {}'.format(nota, disciplina)
print(texto)

print(disciplina[0:6])  # mostrar apenas 6 caracteres da variavel
tamanho = len(disciplina)
print(tamanho)

nome = input('Qual seu nome?')
print('Olá {}, seja bem-vindo!'.format(nome))
# colocar float/int antes do input para númericos

x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
res = 'O resultado da soma de {} com {} é {}.'.format(x, y, x + y)
print(res)
