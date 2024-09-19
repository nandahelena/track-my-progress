// Importa o módulo 'fs' para ler a entrada do usuário
const fs = require("fs");

// Lê a entrada do usuário e a divide em linhas
entrada = fs.readFileSync(0, "utf8");
entrada = entrada.split("\n");

// A primeira linha é o tamanho do input e a segunda linha são os números separados por espaços
tamanho_input = entrada[0];
input = entrada[1].split(" ");

// Inicializa um contador para a quantidade de sequências encontradas
quant_naturais = 0;

// Percorre o array de números para encontrar sequências específicas
for (let i = 0; i <= tamanho_input; i++) {
    // Verifica se a sequência '1 0 0' está presente a partir da posição i
    if (input[i] == 1 && input[i + 1] == 0 && input[i + 2] == 0) {
        quant_naturais++; // Incrementa o contador se a sequência for encontrada
    }
}

// Mostra no console o número de sequências encontradas
console.log(quant_naturais);