#include <stdio.h>
#include <string.h>

int main(){
    // Declara três arrays de caracteres para armazenar a string de entrada, as vogais e as consoantes
    char s[60], v[60], c[60];

    // Lê a string de entrada do usuário
    scanf("%s", s);

    // Variáveis para controle de loops e contadores para vogais e consoantes
    int i, cont1 = 0, cont2 = 0;

    // Loop para percorrer cada caractere da string de entrada
    for(i = 0; i < strlen(s); i++){
        // Verifica se o caractere atual é uma vogal
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            // Adiciona a vogal ao array de vogais e incrementa o contador
            v[cont1] = s[i];
            cont1++;
        } else {
            // Se não for uma vogal, adiciona ao array de consoantes e incrementa o contador
            c[cont2] = s[i];
            cont2++;
        }
    }

    // Adiciona o caractere nulo ao final das strings de vogais e consoantes para garantir que sejam tratadas como strings válidas
    v[cont1] = '\0';
    c[cont2] = '\0';

    // Imprime as vogais e consoantes separadamente
    printf("Vogais: %s\n", v);
    printf("Consoantes: %s\n", c);

    return 0;
}
