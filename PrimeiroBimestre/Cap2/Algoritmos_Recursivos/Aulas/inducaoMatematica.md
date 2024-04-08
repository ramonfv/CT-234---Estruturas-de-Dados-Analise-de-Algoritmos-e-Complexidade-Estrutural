# Princípio de indução finita

A indução matemática é uma técnica de prova usada para demostrar que uma propriedade é verdadeira por meio de proposições. 
Seja P(X) uma propriedade sobre o número natual $x \geq x_{0}$, sendo x_{0} um número natural fixado. 

Para provar que P_{X} pode ser provada por indução matemática para todo $x \geq x_{0}$, basta provar que:

1. **Base de Indução**: Prove que a propriedade é verdadeira para os casos básicos $x = x_{0}$ ou $x = x_{1}$.
2. **Hipótese indutiva**: Supomos que P seja verdadeira para o caso genérico $X=N$.
3. **Passo indutivo**: Demostrarmos que P também é verdadeira para o caso $X=N+1$.

Hipótese: como a proposição vale para o caso inical e o passo é correto, então essa proposição é válida para todos os casos subsequentes.

## Exemplo: Dominó

- **Proposição**: Numa sequência de peças de dominóque estejam em pé, suficientemente próximas umas das outras, se a primeira peça cair, todas as demais também vão cair.

- Prova por indução:
    - Base: A primiera peça caiu (Força exeterna).
    - Hipótese indutiva: Supomos que a n-ésima tenha caído também.
    - Passo indutivo: Como a e-nésima peça caiu e ela está suficientemente próxima da seguinte, então a peça (n+1)-enésima peça também irá cair.


## Passo a passo para resolver questões de indução matemática

1. **Entenda o Problema**: Leia a afirmação que você precisa provar cuidadosamente. Certifique-se de entender o que a afirmação está dizendo e o que você precisa provar.

2. **Base da Indução**: Verifique se a afirmação é verdadeira para o menor valor possível de $n$. Isso geralmente é $n = 0$ ou $n = 1$, dependendo do problema.

3. **Hipótese de Induçã**o: Assuma que a afirmação é verdadeira para algum $n = k$. Isso é chamado de hipótese de indução.

4. **Passo de Indução**: O próximo passo é provar que a afirmação é verdadeira para $n = k + 1$. Isso geralmente envolve manipulação algébrica. Tente expressar a afirmação para $n = k + 1$ em termos da afirmação para $n = k$.

5. **Identifique Padrões**: Durante o passo de indução, tente identificar padrões ou estruturas que se repetem. Isso pode envolver fatores comuns, termos que aparecem em ambos os lados da equação, ou outras estruturas que você pode usar para simplificar a expressão.

6. **Use a Hipótese de Indução**: Em algum ponto, você precisará usar a hipótese de indução para mostrar que a afirmação para $n = k + 1$ é verdadeira. Isso geralmente envolve substituir a afirmação para $n = k$ na expressão que você está tentando simplificar.

7. **Conclusão**: Se você conseguiu mostrar que a afirmação é verdadeira para $n = k + 1$ usando a hipótese de indução, então você concluiu a prova. A afirmação é verdadeira para todos os valores de $n$ a partir do valor base que você verificou no início.


O grande foco aqui deve ser:

- **Identificar padrões** é uma parte crucial da resolução de problemas de indução matemática. Aqui estão algumas dicas para ajudá-lo a identificar padrões:

1. **Familiarize-se com Fórmulas Comuns**: Algumas fórmulas aparecem com frequência em problemas de indução, como a soma dos primeiros $n$ números naturais, a soma dos primeiros $n$ quadrados, a soma dos primeiros $n$ cubos, etc. Conhecer essas fórmulas pode ajudá-lo a identificar padrões mais rapidamente.

2. **Pratique a Manipulação Algébrica**: Muitas vezes, você precisará manipular a expressão para $n = k + 1$ para que ela se pareça com a expressão para $n = k$. Isso pode envolver expandir binômios, fatorar expressões, combinar termos semelhantes, etc.

3. **Procure por Recorrências**: Em muitos problemas de indução, a expressão para $n = k + 1$ contém a expressão para $n = k$ de alguma forma. Isso é chamado de recorrência. Identificar essa recorrência pode ser a chave para resolver o problema.

4. **Use a Hipótese de Indução**: Lembre-se de que você está assumindo que a afirmação é verdadeira para $n = k$. Tente substituir essa afirmação na expressão que você está tentando simplificar. Isso pode revelar um padrão.

5. **Não Desista Cedo Demais**: Às vezes, o padrão não é imediatamente óbvio. Você pode precisar manipular a expressão de várias maneiras diferentes antes de ver o padrão. Se você está preso, tente abordar o problema de uma direção diferente.

6. **Pratique, Pratique, Pratique**: Quanto mais problemas de indução você resolver, mais fácil será identificar padrões. Cada problema que você resolve aumenta sua experiência e melhora suas habilidades de resolução de problemas.

Onde práticar?

Livros de Texto e Recursos Online: Use livros de texto de matemática discreta ou álgebra abstrata que tenham seções dedicadas à indução matemática. Muitos desses livros terão exercícios de prática no final de cada capítulo. Recursos online, como Khan Academy ou sites de matemática universitária, também podem ter problemas de prática.

Resolva Problemas Passo a Passo: Ao resolver problemas de indução, certifique-se de seguir cada passo do processo: base da indução, hipótese de indução e passo de indução. Isso ajudará a reforçar sua compreensão do método.



## Exmplo: Divisão

Demonstre que, para $x  \gt 1$ e $n \gt 0$, $x^n - 1$ é divisível por $x-1$.

- Base da indução: Para $n = 1$, temos $x^1 - 1 = x - 1$, que é claramente divisível por $x - 1$.

- Passo da indução: Suponha que a proposição seja verdadeira para algum $n = k$, ou seja, $x^k - 1$ é divisível por $x - 1$. 
Precisamos mostrar que a proposição é verdadeira para $n = k + 1$.

    - Começamos com a expressão $x^{k+1} - 1$.
    - Podemos reescrever isso como $x * x^k - 1$.
    - Agora, adicionamos e subtraímos $x^k$ para obter $x * x^k - x^k + x^k - 1$.
    - Isso pode ser reescrito como $x^k * (x - 1) + (x^k - 1)$.
    - Pela hipótese de indução, sabemos que $x^k - 1$ é divisível por $x - 1$.
    - Além disso, $x^k * (x - 1)$ é claramente divisível por $x - 1$.
    - Portanto, a soma de dois números que são divisíveis por $x - 1$ também é divisível por $x - 1$.
    - Isso mostra que $x^{k+1} - 1$ é divisível por $x - 1$.

Portanto, por indução matemática, podemos concluir que para todo $x > 1$ e $n > 0$, $(x^n) - 1$ é divisível por $x - 1$.

## Exercício: Demonstre por indução matemática

- $n^3 + 2n$:

- Base da indução: Para $n = 0$, temos $0^3 + 2*0 = 0$, que é claramente divisível por 3.

- Passo da indução: Suponha que a proposição seja verdadeira para algum $n = k$, ou seja, $k^3 + 2*k$ é divisível por 3. Precisamos mostrar que a proposição é verdadeira para $n = k + 1$.

    - Começamos com a expressão $(k+1)^3 + 2*(k+1)$.
    - Podemos reescrever isso como $k^3 + 3*k^2 + 3*k + 1 + 2*k + 2$.
    - Isso pode ser reescrito como $(k^3 + 2*k) + 3*k^2 + 3*k + 3$.
    - Pela hipótese de indução, sabemos que $k^3 + 2*k$ é divisível por 3.
    - Além disso, $3*k^2 + 3*k + 3$ é claramente divisível por 3, pois é um múltiplo de 3.
    - Portanto, a soma de dois números que são divisíveis por 3 também é divisível por 3.
    - Isso mostra que $(k+1)^3 + 2*(k+1)$ é divisível por 3.

Portanto, por indução matemática, podemos concluir que para todo $n >= 0$, $n^3 + 2n$ é divisível por 3.

----------------------

-  $2^0 + 2^1 + 2^2 + ... + 2^n = 2^{n+1} - 1$

Base da Indução: Verifique se a afirmação é verdadeira para o menor valor possível de $n$. Neste caso, vamos verificar para $n = 0$:

$2^0 = 2^{0+1} - 1$

$1 = 2 - 1$

$1 = 1$

A afirmação é verdadeira para $n = 0$.

Hipótese de Indução: Assuma que a afirmação é verdadeira para algum $n = k$. Ou seja, assuma que:

$2^0 + 2^1 + 2^2 + ... + 2^k = 2^{k+1} - 1$

Passo de Indução: O próximo passo é provar que a afirmação é verdadeira para $n = k + 1$. Ou seja, precisamos provar que:

$2^0 + 2^1 + 2^2 + ... + 2^k + 2^{k+1} = 2^{k+2} - 1$

Começamos adicionando $2^{k+1}$ em ambos os lados da equação da hipótese de indução:

$2^0 + 2^1 + 2^2 + ... + 2^k + 2^{k+1} = (2^{k+1} - 1) + 2^{k+1}$

Simplificando o lado direito da equação, obtemos:

$2^0 + 2^1 + 2^2 + ... + 2^k + 2^{k+1} = 2 * 2^{k+1} - 1$

$2^0 + 2^1 + 2^2 + ... + 2^k + 2^{k+1} = 2^{k+2} - 1$

Portanto, a afirmação é verdadeira para $n = k + 1$.

Conclusão: Portanto, por indução matemática, a afirmação $2^0 + 2^1 + 2^2 + ... + 2^n = 2^{n+1} - 1$ é verdadeira para todos $n \geq 0$.

---------------
- $2^-1 + 2^-2 + 2^-3 + \cdot\cdot\cdot + 2^{n} < -1$, para $n > 0$

Para provar a afirmação $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-n} < 1$ usando indução matemática, siga os seguintes passos:

Base da Indução: Verifique se a afirmação é verdadeira para o menor valor possível de $n$. Nesse caso, $n = 1$. Temos $2^{-1} = 0.5$, que é menor que 1.

Hipótese de Indução: Assuma que a afirmação é verdadeira para algum $n = k$, ou seja, $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} < 1$.

Passo de Indução: O próximo passo é provar que a afirmação é verdadeira para $n = k + 1$. Isso significa que queremos mostrar que $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} + 2^{-(k+1)} < 1$.

Adicionamos $2^{-(k+1)}$ em ambos os lados da equação da hipótese de indução:

$2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} + 2^{-(k+1)} < 1 + 2^{-(k+1)}$

Como $2^{-(k+1)}$ é menor que 1 (porque $k+1 > 0$), temos que $1 + 2^{-(k+1)} < 2$. Portanto, o lado direito da equação é menor que 2.

Mas, o lado esquerdo da equação é claramente menor que $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} + 2^{-k} = 2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} + 2^{-1} = 1$ (porque $2^{-k} < 2^{-1}$ para $k > 1$).

Portanto, temos que $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-k} + 2^{-(k+1)} < 1$.

E assim, provamos que se a afirmação é verdadeira para $n = k$, então ela também é verdadeira para $n = k + 1$. Isso completa o passo de indução.

Portanto, a afirmação $2^{-1} + 2^{-2} + 2^{-3} + ... + 2^{-n} < 1$ é verdadeira para todo $n \geq 1$.

------------
- A representação binária de um número inteiro $n > 0$ tem exatamente $\lfloor \log_2 n \rfloor + 1$ bits". 

Base da Indução: Verifique se a afirmação é verdadeira para o menor valor possível de $n$. Nesse caso, $n = 1$. A representação binária de 1 é 1, que tem exatamente 1 bit. E $\lfloor \log_2 1 \rfloor + 1 = 0 + 1 = 1$. Portanto, a afirmação é verdadeira para $n = 1$.

Hipótese de Indução: Assuma que a afirmação é verdadeira para algum $n = k$, ou seja, a representação binária de um número inteiro $k$ tem exatamente $\lfloor \log_2 k \rfloor + 1$ bits.

Passo de Indução: O próximo passo é provar que a afirmação é verdadeira para $n = k + 1$. Isso significa que queremos mostrar que a representação binária de $k+1$ tem exatamente $\lfloor \log_2 (k+1) \rfloor + 1$ bits.

Se $k+1$ é uma potência de 2, então $\lfloor \log_2 (k+1) \rfloor = \log_2 (k+1)$ e a representação binária de $k+1$ tem $\log_2 (k+1) + 1$ bits, que é exatamente $\lfloor \log_2 (k+1) \rfloor + 1$ bits.

Se $k+1$ não é uma potência de 2, então $\lfloor \log_2 (k+1) \rfloor = \lfloor \log_2 k \rfloor$ e a representação binária de $k+1$ tem o mesmo número de bits que a representação binária de $k$, que é $\lfloor \log_2 k \rfloor + 1$ bits pela hipótese de indução. Portanto, a representação binária de $k+1$ tem $\lfloor \log_2 (k+1) \rfloor + 1$ bits.

Portanto, a afirmação "A representação binária de um número inteiro $n > 0$ tem exatamente $\lfloor \log_2 n \rfloor + 1$ bits" é verdadeira para todo $n > 0$.

## Recursão ou indução

A ideia de qualquer algoritmo recursivo para um problema é igual à de uma prova por indução matemática:

1. Se a instância que queremos resolver é pequena, resolva-o diretamente, como puder (Base da indução);
2. Se a instância é grande, reduza-a a uma instância menor do mesmo problema (Hipótese de indução);
3. Depois de resolvida a instância menor, volte à instância original (Passo indutivo);

Um algoritmo recursivo precisa apenas mostrar duas coisas ao computador: 
1. Como reduzir uma instância a uma subinstância;
2. omo obter uma solução da instância a partir da solução da subinstância. O computador cuida do resto!

Resolver uma recorrência é:
- Encontrar uma **forma fechada** que dê o valor diretamente em termos de seu parâmetro.

Ou seja, deseja-se obter o valor com base no valor direto e não com base no valor recursivo.

