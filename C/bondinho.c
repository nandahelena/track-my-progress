#include <stdio.h>

int main(){
    // Declara três variáveis inteiras: A, M e S
    int A, M, S;

    // Lê um valor inteiro para A do usuário
    scanf("%d", &A);

    // Lê um valor inteiro para M do usuário
    scanf("%d", &M);

    // Calcula a soma de M e A e armazena o resultado em S
    S = M + A;

    // Verifica se o valor de S é menor ou igual a 50
    if (S <= 50){
        // Se S é menor ou igual a 50, imprime "S"
        printf("S");
    } else {
        // Se S é maior que 50, imprime "N"
        printf("N");
    }

    return 0;
}
