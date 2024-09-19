#include <stdio.h>

int main(){
    // Declara um array de inteiros com 10 elementos, uma variável para controle de fluxo (sn), 
    // uma variável de iteração (i) e uma variável para armazenar o valor a ser procurado (va)
    int v[10], sn = 1, i, va;

    // Lê 10 valores inteiros do usuário e armazena no array v
    for(i = 0; i < 10; i++){
        scanf("%d", &v[i]);
    }

    // Lê o valor que será procurado no array
    scanf("%d", &va);

    // Loop para percorrer o array e verificar se o valor va está presente
    for(i = 0; i < 10; i++){
        // Se o valor for encontrado, imprime "SIM", altera sn para 0 e encerra o loop
        if(v[i] == va){
            printf("SIM");
            sn = 0;
            break;
        }
    }

    // Se o valor não foi encontrado (sn ainda é 1), imprime "NAO"
    if(sn == 1){
        printf("NAO");
    }

    return 0;
}
