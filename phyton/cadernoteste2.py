def servicoCao():
    while True:
        serv = input(
            'Escolha o serviço desejado:\nBA - Banho\nTO - Tosa\nBT - Banho e Tosa>>')
        if serv == 'BA':
            return 10.00
        elif serv == 'TO':
            return 20.00
        elif serv == 'BT':
            return 25.00
        else:
            print('Caracteres inválidos, digite novamente')
            continue


def pesoCao():
    while True:
        try:
            pesoC = float(input('Entre com o peso do cachorro:'))
            if 0 <= pesoC <= 10:
                return 1.5
            elif 10 < pesoC <= 20:
                return 2.0
            elif 20 < pesoC <= 30:
                return 2.5
            elif 30 < pesoC <= 40:
                return 3.0
            elif pesoC > 40:
                return 4.0
            else:
                print('Não aceitamos cachorros com peso negativo.')
                continue
        except ValueError:
            print('Pare de digitar valores não numéricos. Tente novamente.')
            continue


def peloCao():
    while True:
        peloC = input(
            'Entre com o pelo do cachorro:\nC - Curto\nM - Médio\nL - Longo>>')
        if peloC == 'C':
            return 1.5
        elif peloC == 'M':
            return 2.0
        elif peloC == 'L':
            return 2.5
        else:
            print('Caracteres inválidos, digite novamente')
            continue


print('Bem vindo ao Petshop da Luana Franco Trevizani')
print('O valor total foi de: R${:.2f}'.format(
    servicoCao() * pesoCao() * peloCao()))
