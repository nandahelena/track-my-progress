// Função que calcula o fatorial de um número de forma recursiva
function fat(n){
    // Se n for 1 ou 0, retorna 1 (caso base)
    if(n == 1 || n == 0){
        return 1;
    }
    // Retorna n multiplicado pelo fatorial de n-1
    return n * fat(n - 1);
}

// Lê a entrada do usuário e a armazena na variável 'fs'
const fs = require("fs").readFileSync(0, "utf8");
// Converte a entrada para um número inteiro
let entrada = parseInt(fs);

// Chama a função fatorial com a entrada e exibe o resultado no console
console.log(fat(entrada));
