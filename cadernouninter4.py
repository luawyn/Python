listaProdutos = []
# -------- Começo cadastrarProduto ------------


def cadastrarProduto(codigo):
    print('Você selecionou a opção de cadastrar produto.')
    print('Cógido do Produto: {}'.format(codigo))
    nome = input('Por favor, entre com o NOME do produto: ')
    fabricante = input('Por favor, entre com o FABRICANTE do produto: ')
    valor = float(input('Por favor, entre com o VALOR(R$) do produto: '))
    dicionarioProduto = {'codigo': codigo,
                         'nome': nome,
                         'fabricante': fabricante,
                         'valor': valor}
    listaProdutos.append(dicionarioProduto.copy())

# --------- Fim cadastrarProduto ---------------

# -------- Começo consultarProduto ------------


def consultarProduto():
    while True:
        print('Você selecionou a opção de consultar produto.')
        opConsultar = int(input(
            'Escolha a opção desejada:\n1 - Consultar todos os produtos\n2 - Consultar Produtos por Código\n3 - Consultar Produtos por Fabricante\n4 - Retornar\n>>'))
        if opConsultar == 1:
            for produto in listaProdutos:
                for key, value in produto.items():
                    print("{} : {}".format(key, value))
        elif opConsultar == 2:
            entrada = int(input('Digite o CÓDIGO do Produto:'))
            for produto in listaProdutos:
                if (produto['codigo'] == entrada):
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
        elif opConsultar == 3:
            entrada = (input('Digite o FABRICANTE do(s) Produto(s): '))
            for produto in listaProdutos:
                if (produto['fabricante'] == entrada):
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
        elif opConsultar == 4:
            break
        else:
            print('Caractere inválido, digite novamente.')
# --------- Fim consultarProduto -------------

# -------- Começo removerProduto ------------


def removerProduto():
    print('Você selecionou a opção de remover produto.')
    entrada = int(input('Digite o código do produto a ser removido: '))
    for produto in listaProdutos:
        if (produto['codigo'] == entrada):
            listaProdutos.remove(produto)
# --------- Fim removerProduto --------------


# -------- Começo Main ------------
print('Bem-vindo ao Controle de Estoque da Mercearia da Luana Franco Trevizani')
registroProduto = 0
while True:
    opcao = int(input(
        'Escolha a opção Desejada: \n1 - Cadastrar Produto\n2 - Consultar Produto(s)\n3 - Remover Produto\n4 - Sair \n>>'))
    if opcao == 1:
        registroProduto = registroProduto + 1
        cadastrarProduto(registroProduto)
    elif opcao == 2:
        consultarProduto()
    elif opcao == 3:
        removerProduto()
    elif opcao == 4:
        print('Programa finalizado')
        break
    else:
        print('Caractere inválido, digite novamente.')
# --------- Fim main -----------
