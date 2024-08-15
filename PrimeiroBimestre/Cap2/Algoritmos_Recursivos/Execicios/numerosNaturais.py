# Imprimir os n primeiros números naturais em odem crescente    

def naturaisCrescente(n):
    if n == 1:
        print(1)
    else:
        naturaisCrescente(n-1)
        print(n)


def naturaisDecrescente(n):
    if n == 1:
        print(1)
    else:
        print(n)
        naturaisDecrescente(n-1)


if __name__ == '__main__':
    n = int(input('Digite um numero: '))
    naturaisCrescente(n)
    # naturaisDecrescente(n)