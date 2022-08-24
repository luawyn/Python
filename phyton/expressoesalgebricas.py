# O somatório dos 5 primeiros números inteiros e positivos
print(1 + 2 + 3 + 4 + 5)

# A média entre 23, 19 e 31
print((23 + 19 + 31) / 3)

# O número de vezes que 73 cabe em 403
print(403 // 73)  # // somente a parte inteira

# A sobra quando 403 é dividido por 73
print(403 % 73)

# 2 elevado a 10 potência
print(2 ** 10)

# O valor absoluto da diferença entre 54 e 57
print(abs(54-57))

# O menor valor entre 34, 29 e 31
print(min(34, 29, 31))

# desconto de produto

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}'.format(preco, p))
print('O valor  calculado de desconto: {}'.format(final))
