def soma(x=0, y=0, z=0):
    """
    Função que soma até 3 valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: soma inteira
    """
    return x+y+z


print(soma(3, 2))
help(soma)


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat


x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('{}! = {}'.format(x, fatorial(x)))
