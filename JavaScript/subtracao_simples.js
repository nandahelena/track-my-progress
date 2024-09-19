const fs = require("fs");

// Lê os dados de entrada do usuário (ou do terminal)
entrada = fs.readFileSync(0, "utf8");

// Divide a entrada em linhas (quebra cada linha do texto recebido)
entrada = entrada.split("\n");

// Pega a primeira linha, transforma em número e guarda em 'a'
var a = parseInt(entrada[0]);

// Pega a segunda linha, transforma em número e guarda em 'b'
var b = parseInt(entrada[1]);

// Mostra no console a diferença entre 'a' e 'b'
console.log(a - b);
