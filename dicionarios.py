game = {'nome': 'Super Mario', 'desenvolvedora': 'Nintendo', 'ano': 1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# values: obtem somente os dados
# keys: obtem somente chave
# items : obtem os dados e chaves

print(game.values())

for i in game.values():  # maneira que deixa mais apresentável
    print(i)

for i in game.keys():
    print(i)

for i, j in game.items():
    print('{} = {}'.format(i, j))

    games = {}
    games = []
    for i in range(3):
        game['nome'] = input('Qual o nome do jogo?')
        game['videogame'] = input('Para qual video-game ele foi lançado?')
        game['ano'] = input('Qual o ano de lançamento?')
        games.append(game.copy())
print('-' * 20)
for e in games:
    for i, j in e.items():
        print('O campo {} tem o valor {}'.format(i, j))
