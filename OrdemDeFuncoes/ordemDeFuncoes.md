# Crescimento de Funções

Ordem de funções é um tópico que abordará como o tempo de execução de um algoritmo e o espaço ocupado na memória crescem em relação as entradas do algoritmo.

Mas o que é o tempo de execução de um algoritmo? como é definido?

<!-- Partindo do ponto que estamos trabalhando com processadores com a mesma arquitetura, além de desconsiderar ciclos de clock dos processadores, memória disponível, linguagem de programação... -->

**O programa abaixo, retorna o valor da soma de todos os n itens da lista**:

```
def soma(lista):
    resultadoSoma = 0
    for elemento in lista:
        resultadoSoma += elemento
    return resultadoSoma

soma([1,2,3,4,5])
```


O tempo de execução de um algoritmo, é o tempo total que o processador leva para executar todas as instruções do algoritmo. Segundo TANENBAUM, A. S., & AUSTIN, T. (2013), o processador executa cada instrução em uma série de etapas, que podem ser condensadas em:

- **Trazer a próxima instrução da memória até o registrador de instrução**: A CPU busca a próxima instrução, que é o início do loop "for".
- **Alterar o contador de programa para que aponte para a próxiam instrução**: O contador de programa é atualizado para apontar para a primeira instrução dentro do loop.
- **Determinar o tipo de instrução trazida**: A CPU reconhece que deve iterar sobre os elementos do vetor..
- **Se ainstrução for uma palabra na memória determinar onde está**: A CPU acessa os elementos do vetor na memória.
- **Trazer a palavra para dentro de um registrador da CPU, se necessário**: Os elementos do vetor são carregados na CPU, conforme necessário.
- E**xecutar a instrução**: A CPU executa a instrução de soma para adicionar cada elemento ao total (variável, soma).
- **Voltar à etapa 1 para executar a instrução seguinte**: O processo é repetido até que todos os elementos do vetor tenham sido somados.

Dessa forma, o tempo de execução total do algoritmo é a soma do tempo que a CPU leva para executar todas essas instruções.

No contexto da disciplina do curso, todos os fatores externos como poder de processamento, linguagem de programação, disponibilidade de memória, dentre outros, são desconsiderados e o tempo de execução dos algoritmos são avaliados em relação ao tamanho da entrada. Isso significa que o tempo de execução do algoritmo é proporcional ao tamanho da entrada