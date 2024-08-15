# Algoritmo recursivo para eoncontrar o n-esimo numero da sequencia de Fibonacci

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == '__main__':
    n = int(input('Digite um numero: '))
    print(f'O {n}-esimo numero da sequencia de Fibonacci é {fib(n)}')