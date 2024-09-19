// Importa o módulo 'fs' e lê a entrada do usuário, dividindo em linhas
const fs = require("fs").readFileSync(0, "utf8").split("\n");

// Converte as entradas em números
const tempos = fs.map(Number);

// Armazena os três tempos em variáveis
let tempo1 = tempos[0];
let tempo2 = tempos[1];
let tempo3 = tempos[2];

// Encontra o menor, o maior e o tempo médio usando Math.min e Math.max
let menor_tempo = Math.min(tempo1, tempo2, tempo3);
let maior_tempo = Math.max(tempo1, tempo2, tempo3);
let meio_tempo = tempo1 + tempo2 + tempo3 - menor_tempo - maior_tempo;

// Mostra no console a posição (índice + 1) de cada tempo (menor, médio e maior)
console.log(tempos.indexOf(menor_tempo) + 1);
console.log(tempos.indexOf(meio_tempo) + 1);
console.log(tempos.indexOf(maior_tempo) + 1);
