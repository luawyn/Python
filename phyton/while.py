#inicial = int(input('Qual valor deseja iniciar a contagem?'))
#final = int(input('Qual valor deseja encerrar a contagem?'))
#x = inicial
# while (x <= final):
#    if (x % 2 == 0):
#        print(x)
#    x = x + 1

#soma = 0
#cont = 1
# while (cont <= 5):
#    x = float(input('Digite a {}ª nota:'.format(cont)))
#    soma = soma + x
#    cont = cont + 1
#    media = soma / 5
#print('Média final: {}'.format(media))

while True:
    nome = input('Qual o seu nome?')
    if (nome != 'Luana'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == '123456'):
        break
print('Acesso concedido')
