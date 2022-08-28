listaEstudantes = []
# -------- Começo cadastrarEstudante ------------


def cadastrarEstudante(ru):
    print('Bem-vindo ao cadastro de estudantes')
    print('O RU do estudante a ser cadastrado é: {}'.format(ru))
    nome = input('Digite o nome do estudante: ')
    turma = input('Digite a turma do estudante: ')
    dicionarioEstudante = {'ru': ru,
                           'nome': nome,
                           'turma': turma}
    listaEstudantes.append(dicionarioEstudante.copy())

# --------- Fim cadastrarEstudante

# -------- Começo consultarEstudante ------------


def consultarEstudante():
    while True:
        try:
            print('Bem-vindo ao consultar de estudantes')
            opConsultar = int(input(
                'Entre com a opção desejada:\n1 - Consultar todos os estudantes\n2 - Consultar por RU\n3 - Consultar por turma\n4 - Retornar\n>>'))
            if opConsultar == 1:
                print('Bem vindo ao consultar TODOS')
                for estudante in listaEstudantes:
                    for key, value in estudante.items():
                        print("{} : {}".format(key, value))
            elif opConsultar == 2:
                print('Bem vindo ao consultar RU')
                entrada = int(input('Digite o RU desejado:'))
                for estudante in listaEstudantes:
                    if (estudante['ru'] == entrada):
                        for key, value in estudante.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                print('Bem vindo ao consultar TURMA')
                entrada = (input('Digite a turma desejado:'))
                for estudante in listaEstudantes:
                    if (estudante['turma'] == entrada):
                        for key, value in estudante.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                break
            else:
                print('Caractere inválido')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')
# --------- Fim consultarEstudante

# -------- Começo removerEstudante ------------


def removerEstudante():
    print('Bem-vindo ao remover de estudantes')
    entrada = int(input('Digite o RU desejado:'))
    for estudante in listaEstudantes:
        if (estudante['ru'] == entrada):
            listaEstudantes.remove(estudante)
# --------- Fim removerEstudante


# -------- Começo Main ------------
print('Bem-vindo ao programa controle de estudantes da Luana Franco Trevizani')
registroAcademico = 0
while True:
    try:
        opcao = int(input(
            'Digite a opção Desejada: \n1 - Cadstrar Estudante\n2 - Consultar Estudante\n3 - Remover Estudante\n4 - Sair \n>>'))
        if opcao == 1:
            registroAcademico = registroAcademico + 1
            cadastrarEstudante(registroAcademico)
        elif opcao == 2:
            consultarEstudante()
        elif opcao == 3:
            removerEstudante()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Caractere inválido')
            continue
    except:
        print('Pare de digitar valores não inteiros')
# --------- Fim main -----------
