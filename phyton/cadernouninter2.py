# Questão 2 de 4

somaPrecos = 0
print('Bem-vindo a Pizzaria da Luana Franco Trevizani')
print('------------------------Cardápio-----------------------')
print('| Código | Nome do Sabor | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana    |    R$ 20,00 |     R$ 26,00 |')
print('|   22   | Margherita    |    R$ 20,00 |     R$ 26,00 |')
print('|   23   | Calabresa     |    R$ 25,00 |     R$ 32,50 |')
print('|   24   | Toscana       |    R$ 30,00 |     R$ 39,00 |')
print('|   25   | Portuguesa    |    R$ 30,00 |     R$ 39,00 |')
print('-------------------------------------------------------')

while True:

    # recebe o tamanho da pizza
    tamanho = input('Qual tamanho de pizza que deseja (M/G): ')
    if tamanho != 'M' and tamanho != 'G':  # se tamanho for diferente de M ou G, printa e reinicia o laço
        print('Operação Inválida')
        continue
    # recebe o código da pizza desejado
    codigo = input('Entre com o código do sabor desejado: ')
    # Se o código for igual a 21 e o tamanho igual a M, irá somar o valor ao contador e printar o pedido do usuário (se repete em todos os elif)
    if codigo == '21' and tamanho == 'M':
        somaPrecos = somaPrecos + 20
        print('Você pediu uma pizza Napolitana Média')
    elif codigo == '21' and tamanho == 'G':
        somaPrecos = somaPrecos + 26
        print('Você pediu uma pizza Napolitana Grande')
    elif codigo == '22' and tamanho == 'M':
        somaPrecos = somaPrecos + 20
        print('Você pediu uma pizza Margherita Média')
    elif codigo == '22' and tamanho == 'G':
        somaPrecos = somaPrecos + 26
        print('Você pediu uma pizza Margherita Grande')
    elif codigo == '23' and tamanho == 'M':
        somaPrecos = somaPrecos + 25
        print('Você pediu uma pizza Calabresa Média')
    elif codigo == '23' and tamanho == 'G':
        somaPrecos = somaPrecos + 32.5
        print('Você pediu uma pizza Calabresa Grande')
    elif codigo == '24' and tamanho == 'M':
        somaPrecos = somaPrecos + 30
        print('Você pediu uma pizza Toscana Média')
    elif codigo == '24' and tamanho == 'G':
        somaPrecos = somaPrecos + 39
        print('Você pediu uma pizza Toscana Grande')
    elif codigo == '25' and tamanho == 'M':
        somaPrecos = somaPrecos + 30
        print('Você pediu uma pizza Portuguesa Média')
    elif codigo == '25' and tamanho == 'G':
        somaPrecos = somaPrecos + 39
        print('Você pediu uma pizza Portuguesa Grande')
    else:  # se for digitada algo que não seja o número do código e o tamanho da pizza, irá printar que a opção é inválida e repetir o laço.
        print('Opção Inválida')
        continue

    novoProduto = input(
        'Deseja pedir mais alguma coisa? \n 1 - Sim \n 0 - Não \n')  # recebe mais pedido ao total da conta ou não
    if novoProduto == '1':
        # irá continuar o laço e somar mais um pedido ao contador para a conta do usuário.
        continue
    else:  # se digitado qualquer coisa que não seja '1'
        print('O total a ser pago é: R${:.2f}'.format(somaPrecos))
        break  # irá mostrar o valor total e parar o laço.
