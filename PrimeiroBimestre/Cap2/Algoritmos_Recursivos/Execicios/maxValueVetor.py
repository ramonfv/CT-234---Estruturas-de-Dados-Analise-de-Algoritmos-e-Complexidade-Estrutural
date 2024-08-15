# Encontrar o valor máximo presente em um vetor

def maxValue(v, n):
    if n == 1:
        return v[0]
    else:
        max = maxValue(v, n-1)
        if max > v[n-1]:
            return max
        else:
            return v[n-1]

if __name__ == '__main__':
    v = [5, 10, 3, 2, 7, 9, 1, 8, 6, 4]
    print(f'O maior valor do vetor é {maxValue(v, len(v))}')