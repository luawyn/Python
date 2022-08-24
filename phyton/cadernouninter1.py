# Questão 1 de 4
print('Bem vindo a Loja da Luana Franco Trevizani')
precoProduto = float(input('Entre com o valor do produto: '))
quantidadeProduto = int(input('Entre com a quantidade do produto: '))
res = precoProduto * quantidadeProduto

# Se a quantidade do produto for menor ou igual a 4 mostrará o valor de desconto de 0% (sem desconto)
if quantidadeProduto <= 4:
    print('O valor sem desconto foi: R${:.2f}'.format(res))
    print('O valor com desconto foi: R${:.2f}'.format(res))
# Se a quantidade do produto for maior ou igual a 5 e menor ou igual a 19 mostrará o valor de desconto de 3%
elif quantidadeProduto >= 5 and quantidadeProduto <= 19:
    print('O valor sem desconto foi: R${:.2f}'.format(res))
    print('O valor com desconto foi: R${:.2f}'.format(
        res * 0.97))  # desconto de 3%
# Se a quantidade do produto for maior ou igual a 20 e menor ou igual a 99 mostrará o valor de desconto de 6%
elif quantidadeProduto >= 20 and quantidadeProduto <= 99:
    print('O valor sem desconto foi: R${:.2f}'.format(res))
    print('O valor com desconto foi: R${:.2f}'.format(
        res * 0.94))  # desconto de 6%
else:  # Se a quantidade do produto for maior ou igual a 100 mostrará o valor de desconto de 10%
    print('O valor sem desconto foi: R${:.2f}'.format(res))
    print('O valor com desconto foi: R${:.2f}'.format(
        res * 0.9))  # desconto de 10%
