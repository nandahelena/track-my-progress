// Importa o módulo 'fs' e lê a entrada do usuário
const fs = require("fs").readFileSync(0, "utf8");

// Define um array com as vogais
const vogais = ["a", "e", "i", "o", "u"];
let vogaisDaPalavra = ""; // Inicializa uma string vazia para armazenar as vogais encontradas

// Percorre cada letra da entrada
for (let letra of fs) 
    // Se a letra for uma vogal, adiciona à string 'vogaisDaPalavra'
    if (vogais.includes(letra)) 
        vogaisDaPalavra += letra;

// Inverte a string de vogais e junta as letras em uma nova string
let vogaisInversas = [...vogaisDaPalavra].reverse().join("");

// Compara as vogais inversas com as vogais originais e mostra "S" se forem iguais, "N" caso contrário
vogaisInversas == vogaisDaPalavra ? console.log("S") : console.log("N");
