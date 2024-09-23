// Importa o módulo 'fs' e lê a entrada padrão, transformando cada linha em um elemento de um array
const entrada = require("fs").readFileSync(0, "utf8").split("\n")

// Inicializa a variável para contar quantas evoluções de Pokémon foram feitas
let pokeEvol = 0

// Lê a primeira linha da entrada, que contém o número de doces disponíveis, e a converte para inteiro
let doces = parseInt(entrada[0])

// Lê as próximas três linhas, que representam a quantidade de doces necessários para evoluir cada Pokémon
// Converte esses valores de string para inteiro e os organiza em ordem crescente
let pokemons = [entrada[1], entrada[2], entrada[3]]
pokemons = pokemons.map(number => parseInt(number)).sort((a,b) => a-b)

// Loop para tentar evoluir os Pokémons enquanto houver doces suficientes
for(let i = 0; i < 3; i++){
    // Verifica se ainda há doces suficientes para evoluir o Pokémon atual (pokemons[i])
	if(doces - pokemons[i] >= 0){
		// Se houver doces suficientes, subtrai a quantidade de doces necessários para essa evolução
		doces -= pokemons[i]
		// Incrementa o contador de evoluções feitas
		pokeEvol++
	} else break // Se não houver doces suficientes, o loop é interrompido
}

// Exibe o número total de evoluções feitas
console.log(pokeEvol)
