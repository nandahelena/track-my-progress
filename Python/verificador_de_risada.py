# Lê uma string do usuário
risada = input()

# Lista de vogais para verificar se um caractere é uma vogal
vogais = ['a', 'e', 'i', 'o', 'u']

# String para armazenar as vogais extraídas da string de entrada
sem_consoante = ''

# Loop para percorrer cada caractere na string de entrada
for i in risada:
    # Se o caractere atual for uma vogal, adiciona à string sem_consoante
    if i in vogais:
        sem_consoante += i

# Verifica se a string sem_consoante é um palíndromo
# Um palíndromo é uma string que é igual a sua própria reversa
if sem_consoante == sem_consoante[::-1]:
    # Se for um palíndromo, imprime "S"
    print("S")
else:
    # Caso contrário, imprime "N"
    print("N")
