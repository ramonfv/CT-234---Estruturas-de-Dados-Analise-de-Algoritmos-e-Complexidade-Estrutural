# programa recursivo que calcula a omsa dos numeros naturais de 1 a n

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

if __name__ == '__main__':
    n = int(input('Digite um numero: '))
    print(f'A soma dos numeros naturais de 1 a {n} é {soma(n)}')