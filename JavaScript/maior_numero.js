// Importa o módulo 'fs' para ler a entrada do usuário
const fs = require("fs");

// Lê a entrada do usuário e a divide em partes (separadas por espaços)
let entrada = fs.readFileSync(0, "utf8").split(" "); 

// Cria um array vazio para armazenar os números inteiros
let entrada_inteiros = [];

// Converte cada parte da entrada em um número inteiro e adiciona ao array
for (let i of entrada) entrada_inteiros.push(parseInt(i));

// Inicializa a variável para armazenar o maior número
let maior_numero = 0;

// Verifica cada número na lista para encontrar o maior
for (let i of entrada_inteiros) {
    if (i > maior_numero) {
        maior_numero = i; // Atualiza 'maior_numero' se encontrar um número maior
    }
}

// Mostra o maior número encontrado no console
console.log(maior_numero);