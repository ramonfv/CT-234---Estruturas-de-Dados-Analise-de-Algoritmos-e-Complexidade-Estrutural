# Cap 2: Algoritmos recursivos

Análogo ao método de indução matemática, algoritmos recursivos podem ser solucionados a partir da prova de indução, composta por:

- Base: Etapa de comprovação, que define um caso válido para a recursão.
- Hipótese Indutiva: Por definição, é uma suposição, válida para um caso genérico.
- Passo Indutivo: É uma demonstração, uma prova de conceito.

Algoritmos recursivos possuem um mecanismo de recursão, em que, durante a execução de um programa, o contexto da etapa anterior é guardado. Isso ocorre por conta do mecanismo de execução baseado no modelo de von neuman, chamado pilha de execução. 

A pilha de execução é composta por, espaço de instruções de programa, área de dados (variáveis estáticas e globais), espaço para chamadas de procedimento (utilizam o SP stack pointer para guardar o contexto de execução, quando há uma chamada recursiva um novo espaço do frame é utilizado) e heap.

Para entendimento da pilha de execução, debugar os exemplos 1 e 2 do capítulo 2.

Para usar ou implementar algoritmos recursivo deve ser levado em consideração os fatores principais da implementação de um algoritmo: Funcionalidade, eficiência e elegância. Os exemplos citados (soma e Fibonacci) são péssimas implementações seguintos os critétios estabelecidos, pois possuem tempo de execução maiores do que as versões iterativas. A ordem de crescimento de ambos os casos (iterativo e recursivo) são as mesmas, no entanto, a pilha de execução é muito menor. No caso do algoritmo recursivo, o stack pointer aumenta proporcionalmente ao número de chamadas, que no pior caso é n-1. Dependendo do tamanho de n pode ocorrer o stack overflow, que é o estouro do limite de memória disponível para uso, o tamanho do frame aumenta no sentido para baixo da pilha e o heap (alocação) cresce no sentido do topo da pila.

Para melhor entendimento de algoritmos recursivos, verificar os exemplos implementados. Utilize o modo de debug para que seja possível entender como a pilha de execução cresce e como é seu funcionamento.


