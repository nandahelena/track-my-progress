// Importa o módulo 'fs' para ler a entrada do usuário
const fs = require("fs");

// Lê a entrada do usuário e a divide em linhas
entrada = fs.readFileSync(0, "utf8").split("\n");

// A primeira linha é a palavra e a segunda linha é a letra que queremos contar
palavra = entrada[0];
letra = entrada[1];

// Inicializa um contador para a letra
letra_num = 0;

// Percorre cada caractere da palavra
for (let i of palavra) {
    // Se o caractere atual for igual à letra, incrementa o contador
    if (letra == i) {
        letra_num++;
    }
}

// Mostra no console o número de vezes que a letra aparece na palavra
console.log(letra_num);