km = int(input('Quantidade de km percorridos:'))
dias = int(input('Quantos dias o carro foi alugado:'))

preco = 60 * dias + 0.15 * km

print('km rodado: {}. Dias Alugados: {}.'.format(
    km, dias))
print('Valor total: R$', preco)
