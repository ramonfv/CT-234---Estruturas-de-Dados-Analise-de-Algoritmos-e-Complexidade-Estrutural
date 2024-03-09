#include <iostream> // Header que contém funcções básicas de entrada e saída

// Existem dois passos para criar e usar uma variável em cpp
// 1º - Declaração: Precisamos definir o tipo de dado
// 2º - Atribuição

int main(){

    int variableOne; // Declaração
    variableOne = 10; // Atribuição
    int variableTwo = 20;

    // Double
    double price = 10.56;

    // caracter - char
    char grade = 'A';
    char alphabetInicial = 'B';

    // Boleano (true or false)
    bool student = true;
    bool oldMan = false;

    // String - palavras, frases...
    std::string name = "Ramon";
    std::string day = "Friday";

    std::cout << "Hello " << name << '\n';
    std::cout << day << '\n';

    return 0;
}
