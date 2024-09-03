# Árvores balanceadas (AVL, Rubro-Negras, B-trees)

## Árvores 

É uma estrutura de dados hierárquica composta por *nós* conectados por *arestas/arcos*. Cada nó tem um pai e pode ter nenhum ou vários filhos. Por ser estruturado através de hierárquia é considerada uma estrutura não linear, diferentemente de arrays e listas.

Existem diferentes tipos de árvores, cada uma com características específicas:

1. **Árvore AVL**: Uma árvore onde a altura de suas subárvores diferem no máximo de uma unidade.
2. **Árvore binária**: Cada nó tem no máximo dois filhos.
3. **Árvore B**: Uma árvore balanceada geralmente usada em bancos de dados e sistemas de arquivos.

Exemplo de uma árvore binária simples
````
        9
       /  \
      5    15
     / \   / \
    3   8 12  20
````

Para que seja considerado uma árvore, a estrutura de dados deve permitir que cada nó seja atingível a partir da raiz através de uma sequência única de arcos, chamada *caminho*. O número de arcos em um caminho é chamado de comprimento do caminho. A *altura* de uma árvore é definida como o maior caminho entre a raiz e todas as folhas (não contamos a raíz). A árvore do exemplo possui caminhos com mesmo tamanho:

- 9 -> 5 -> 3: caminho de tamanho 2 (só existem dois arcos).

Como os demais caminhos possuem o mesmo tamanho, a altura da árvore é 2.

## Árvore de Busca Binária

Na árvore de busca binária, cada nó tem no máximo dois filhos, e a chave (valor) de cada nó é maior que todas as chaves dos nós na subárvore esquerda e menor que todas as chaves dos nós na subárvore direita. Essa propriedade permite realizar buscas, inserções e remoções de forma eficiente, além de: 

Permitir imprimir todas as chaves em sequência ordenada, denominada **percurso de árvore *in-ordem***:

- Percorre a subárvore esquerda em ordem, visita o nó raiz e, então, percorre a subárvore direita em ordem.

Um **percurso de árvore em *pré-ordem*** imprime a raiz antes dos valores das subárvores:
-Percurso em pré-ordem significa que primeiro visita o nó raiz e, em seguida, recursivamente visita a subárvore esquerda e depois a subárvore direita.

Um **percurso de árvore em *pós-ordem*** imprime a raiz depois dos valores em suas subárvore:
- O percurso em pós-ordem segue a ordem de "esquerda, direita, raiz". Isso significa que, antes de visitar o nó raiz, todos os nós da subárvore esquerda e todos os nós da subárvore direita são visitados.

### Buscas

Procedimneto para localizar um determinado valor na árvore. Dado um ponteiro $x$ para raiz da árvore e uma chave $k$ *buscaArvore* retorna um ponteiro para um nó com chave $k$, se existir algum. O processo de busca funciona:

1. Comece na raiz da árvore.
2. Compare o valor que você está procurando com o valor do nó atual.
- Se o valor procurado for igual ao valor do nó atual, você encontrou o valor na árvore e a busca termina.
- Se o valor procurado for menor que o valor do nó atual, vá para a subárvore esquerda.
- Se o valor procurado for maior que o valor do nó atual, vá para a subárvore direita.
3. Repita os passos 2 e 3 até encontrar o valor desejado ou até alcançar um nó nulo 

Transformando isso em um algoritmo, temos algo como:

Exemplo de um algoritmo de busca em uma árvore binária Cormen (2002):
````
buscaArvore(x, k)

if x == Nil ou K == x.chave
    return x
if k < x.chave
    return buscaArvore(x.esquerda, k)
else return buscaArvore(x.direita, k)

````

### Inserção

Para inserir um novo valor $v$ em uma árvore binária $T$, é necessário respeitar a propriedade da árvore binária (**cada nó tem no máximo dois filhos, e a chave de cada nó é maior que todas as chaves dos nós na subárvore esquerda e menor que todas as chaves dos nós na subárvore direita**). Para inserir um valor na árvore, assume-se esse valor como nó ($z$) e que as subarvores a esquerda e direita são vazias, em seguida, a árvore $T$ é modificada de tal forma que insere $z$ na posição correta.

O algoritmo *insereChaveArvore* começa na raíz da árvore e o ponteiro $x$ traça um caminho descentende até um nó que não possua filhos (nil ou vazio) para substituit pelo item de entrada $z$. O procedimento é executado com o auxílio de um ponteiro auxiliar, denominado **ponteiro acompanhante** e é representado por $y$ (os dois ponteiros existem para auxiliar a permutação de endereços de chaves maiores e menores, já que o valor a ser inserido não necessáriamente é um valor alocado na folha, sendo assim para manter a propriedade da árvore binária faz-se necessário utilizar 2 ponteirtos. y é o pai de x).

O procedimento de inserção de um novo valor pode ser compreendido da seguinte foma:
1. Comece na raiz da árvore.
2. Compare o valor a ser inserido com o valor do nó atual.
- Se o valor a ser inserido for menor ou igual ao valor do nó atual, vá para a subárvore esquerda.
- Se o valor a ser inserido for maior que o valor do nó atual, vá para a subárvore direita.
- Repita esse processo até encontrar um nó nulo
3. Insira o novo nó no local onde parou a busca, mantendo as propriedades de uma árvore binária. Se o valor a ser inserido for menor ou igual ao valor do nó atual, o novo nó será inserido como filho esquerdo; se for maior, será inserido como filho direito.

Transformando o procedimento em um algoritmo, temos algo como:

Exemplo de um algoritmo de busca em uma árvore binária Cormen (2002):

````
insereChaveArvore(T, z)

y = Nil
x = T.raiz

while x != Nil
    y = x
    if z.chave < x.chave
        x = x.esquerda
    else
        x = x.direita
z* = y
if y = Nil
    T.raiz = z # arvore era vazia
else if z.chave < y.chave
    y.esquerda = z
else y.direita = z
````

## Árvore AVL

**Definição**: Uma árvore AVL é uma árvore binária de pesquisa que possuia a característica de auto balanceamento, em que a  altura da subárvore à esquerda nunca difere em mais de uma unidade da altura da sua respectiva subárvore direita e vice versa.


No contexto de árvores de busca/pesquisa, árvores AVL garantem que as operações de busca, inserção e remoção sejam realizadas em tempo $\Theta log (n)$. Sendo assim uma AVL é uma estrutura utilizada para garantir o balanceamento de árvores binárias e permitir que operações de busca, inserção e remoção sejam feitas em tempo logarítimo

# Referência 

- Cormen, T. H., Leiserson, C. E., & Rivest, R. L. (1990). Introduction to Algorithms. MIT Press. (Cap 3, seções 12, 13 e 14)




