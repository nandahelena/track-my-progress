// Função que calcula o n-ésimo número de Fibonacci de forma recursiva
function fibonacci(a){
    // Se a entrada for 1 ou 0, retorna 1 (caso base)
    if(a == 1 || a == 0){
        return 1;
    }else{
        // Retorna a soma dos dois números anteriores na sequência de Fibonacci
        return (fibonacci(a-1) + fibonacci(a-2));
    }
}

// Lê a entrada do usuário e a armazena na variável 'fs'
fs = require("fs").readFileSync(0, "utf8");
// Converte a entrada para um número inteiro
fs = parseInt(fs);

// Chama a função Fibonacci com a entrada e exibe o resultado no console
console.log(fibonacci(fs));
