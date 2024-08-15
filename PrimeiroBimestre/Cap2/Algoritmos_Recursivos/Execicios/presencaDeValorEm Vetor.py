# Verificar se um determinado valor está ou não presente em um vetor

def presencaDeValor(v, n, x):
    if n == 1:
        return v[0] == x
    else:
        # return v[n-1] == x or presencaDeValor(v, n-1, x)
        if v[n-1] == x:
            return True
        else:
            return presencaDeValor(v, n-1, x)
    
if __name__ == '__main__':
    v = [5, 10, 3, 2, 7, 9, 1, 8, 6, 4]
    x = int(input('Digite um valor: '))
    if presencaDeValor(v, len(v), x):
        print(f'O valor {x} está presente no vetor')
    else:
        print(f'O valor {x} não está presente no vetor')