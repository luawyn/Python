# Questão 3 de 4
# função 1 - volumeFeijoada
def volumeFeijoada():
    while True:
        print('Menu Volume Feijoada')
        while True:
            try:
                volume = int(input('Entre com a quantidade que deseja(ml): '))
            # se digitado algo que não seja valor numérico ele retorna ao ínicio do laço.
            except ValueError:
                print('Digite apenas valores numéricos. Tente novamente.')
                continue
            break
        if 300 <= volume <= 5000:  # se digitado um valor entre 300 e 5000
            valor = volume * 0.08  # variável para armazena o valor
        else:
            print(
                'Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!')
            continue
        break
    return valor  # retornar o valor da variável

# função 2 - opcaoFeijoada


def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada:')
        opcao = input(
            'Entre com a opção de Feijoada:\nb - Básica (Feijão + paiol + costelinha)\np - Premium (Feijão + paiol + costelinha + partes do porco)\ns - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n>>')
        if opcao == 'b':
            multiplicador = 1
        elif opcao == 'p':
            multiplicador = 1.25
        elif opcao == 's':
            multiplicador = 1.50
        else:
            print('Você não digitou uma opção válida')
            continue
        break
    return multiplicador  # variável que irá armazenar o valor para a multiplicação


def acompanhamentoFeijoada():
    adicional = 0  # variável para armazenar o valor
    while True:
        acomp = input(
            'Deseja mais algum acompanhamento:\n0 - não desejo mais acompanhamentos (encerrar pedido)\n1 - 200g de arroz\n2 - 150g de farofa especial\n3 - 100g de couve cozida\n4 - 1 laranja descascada>>')
        if acomp == '0':
            break
        elif acomp == '1':  # irá adicionar o valor e somar com o que já está dentro da variável, e irá retornar para o início do laço. se repetindo até que o 0 pare o laço
            adicional += 5
            continue
        elif acomp == '2':
            adicional += 6
            continue
        elif acomp == '3':
            adicional += 7
            continue
        elif acomp == '4':
            adicional += 3
            continue
        else:
            print('Você não digitou uma opção válida')
            continue
    return adicional


volume = volumeFeijoada()
opcao = opcaoFeijoada()
adicional = acompanhamentoFeijoada()
total = ((volume * opcao) + adicional)
print('Bem vindo ao Programa de Feijoada da Luana Franco Trevizani')
print('O valor a ser pago é (R$): {:.2f} (volume = {:.2f} * opção = {:.2f} + acompanhamento = {:.2f})'.format(
    total, volume, opcao, adicional))
