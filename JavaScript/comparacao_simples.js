// Importa o módulo 'fs' para ler a entrada do usuário
const fs = require("fs");

// Lê a entrada do usuário (ou do terminal)
let entrada = fs.readFileSync(0, "utf8");

// Divide a entrada em várias linhas e armazena cada linha em um array
let lista_entradas = entrada.split("\n");

// Pega os dois primeiros números, multiplica e transforma em número inteiro, guarda o resultado em 'a1'
let a1 = parseInt(lista_entradas[0] * lista_entradas[1]);

// Pega os dois próximos números, multiplica e transforma em número inteiro, guarda o resultado em 'a2'
let a2 = parseInt(lista_entradas[2] * lista_entradas[3]);

// Verifica qual resultado é maior: se 'a1' for maior, mostra 'a1', senão, mostra 'a2'
a1 > a2 ? console.log(a1) : console.log(a2);