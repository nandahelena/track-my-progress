// O conteúdo da entrada é transformado em uma array de strings, onde cada linha está em um índice diferente
const entrada = require("fs").readFileSync(0, "utf8").split("\n")

// A segunda linha da entrada (entrada[1]) contém os números que representam as bonecas
// Esses números são separados por espaço, e convertidos para inteiros (parseInt)
let bonecas = entrada[1].split(" ").map(number => parseInt(number))

// Cria uma cópia da lista de bonecas e ordena a cópia em ordem crescente
let bonecasOrdered = bonecas.slice().sort((a,b) => a-b)

// Variável para contar quantas bonecas estão fora de ordem
let quantBonecas = 0

// Array que vai armazenar as bonecas que estão fora de ordem
let outOfOrder = []

// Loop para comparar a lista original com a lista ordenada
for(let i = 0; i < bonecas.length; i++){
    // Se o elemento na posição 'i' da lista original for diferente do da lista ordenada,
    // significa que essa boneca está fora de ordem
	if(bonecasOrdered[i] !== bonecas[i]){
		// Adiciona a boneca fora de ordem à lista 'outOfOrder'
		outOfOrder.push(bonecas[i])
		// Incrementa o contador de bonecas fora de ordem
		quantBonecas++
	}
}

// Ordena a lista de bonecas que estavam fora de ordem em ordem crescente
outOfOrder.sort((a,b) => a-b)

console.log(quantBonecas)
console.log(outOfOrder.join(" "))
