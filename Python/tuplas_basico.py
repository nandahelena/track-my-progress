# Lê o número de tuplas a serem criadas
n = int(input())

# Inicializa uma lista vazia para armazenar as tuplas
lista_de_tuplas = []

# Loop para ler as entradas e criar as tuplas
for _ in range(n):
    # Lê uma linha de entrada que contém duas strings separadas por espaço
    linha = input()
    
    # Divide a linha em duas partes usando o espaço como delimitador
    string1, string2 = linha.split()
    
    # Adiciona uma tupla contendo as duas strings à lista de tuplas
    lista_de_tuplas.append((string1, string2))

# Imprime a lista de tuplas
print(lista_de_tuplas)
