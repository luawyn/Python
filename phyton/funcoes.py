def sub2():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        res = num1 - num2
    except:
        print("Algo deu errado...")
    else:
        return res


print(sub2())


def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')


borda('Eu te amo demais mozão')
borda('O que seria de mim sem meu professor particular?')


def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Ops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Sempre executará')


print(div())


def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)


def par(x):
    return x % 2 == 0


def impar(x):
    return not par(x)


imprime_com_condicao(5, par)


def res(x): return x * x


print(res(3))


def soma(x, y): return x + y


print(soma(3, 5))
