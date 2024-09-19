#include <stdio.h>

// Função recursiva que calcula o n-ésimo termo da sequência de Fibonacci
// A sequência de Fibonacci é definida por: 
// F(0) = 1, F(1) = 1 e F(n) = F(n-1) + F(n-2) para n > 1.
int fibo(int n){
    // Caso base: se n for 0 ou 1, retorna 1, pois F(0) = F(1) = 1.
    if(n == 0 || n == 1){
        return 1;
    }else{
        // Chama recursivamente a função para calcular os dois termos anteriores
        return fibo(n-1) + fibo(n-2);
    }
}

int main(){
    int n, fi;
    
    // Lê o valor de 'n' (a posição do termo da sequência de Fibonacci)
    scanf("%d", &n);
    
    // Chama a função 'fibo' para calcular o n-ésimo termo
    fi = fibo(n);
    
    // Imprime o n-ésimo termo da sequência de Fibonacci
    printf("%d", fi);
    
    return 0;
}
