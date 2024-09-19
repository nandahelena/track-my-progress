import re

# Função que verifica se um número é válido com base nos critérios definidos
# Retorna 'YES' se o número tiver 10 caracteres e começar com 7, 8 ou 9. Caso contrário, retorna 'NO'.
def is_valid(number):
    # Usa uma expressão regular para verificar se o número atende aos critérios
    # ^[789] - O número deve começar com 7, 8 ou 9
    # \d{9} - Seguido por exatamente 9 dígitos
    # $ - Fim da string
    return 'YES' if re.fullmatch(r'^[789]\d{9}$', number.strip()) else 'NO'

if __name__ == '__main__':
    # Lê o número de entradas a serem processadas
    n = int(input())

    # Cria uma lista de resultados chamando a função is_valid para cada número de entrada
    results = [
        is_valid(input().strip())
        for _ in range(n)
    ]

    # Imprime todos os resultados, um por linha
    print('\n'.join(results))

        


            
