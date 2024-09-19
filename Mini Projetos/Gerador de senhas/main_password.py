import string
import random

# Função que gera uma senha baseada em um formato fornecido e em uma quantia de caracteres.
def gerar_senha(formato, caracteres):
    # Existem 3 formatos de cadeias de caracteres possíveis.
    cadeias_possiveis = {
        1: string.digits, # Apenas com digitos
        2: string.ascii_letters, # Apenas com letras
        3: string.ascii_letters + string.digits # Com letras e digitos
    }

    # Monta a senha baseado nos parâmetros passados.
    senha = ''.join(random.choices(cadeias_possiveis[formato], k=caracteres))
    return senha


# Cabeçalho
print("----------------------------------")
print("Bem-vindo(a) ao Gerador de Senhas!")
print("----------------------------------")

# Lê uma quantia de caracteres que a senha deve ter
n_caracteres = int(input("Quantos caracteres sua senha deve ter? "))

# Se a quantia for menor ou igual a 0, não é possível criar uma senha. Se não, prossegue e apresenta diferentes formatos de senha.
# Pede ao usuário para escolher um formato de senha entre 1, 2 e 3, se for maior que 3 ou menor/igual a 0, a operação é impossível.
# Se não, a função que gera senhas é chamada e a senha é impressa conforme as preferências do usuário.
if n_caracteres <= 0:
    print(f"Não é possível criar uma senha com {n_caracteres} caracteres. Operação finalizada.")
else:
    formato_senha = int(input("Digite [1] para uma senha só de números, [2] para uma senha só de letras e [3] para incluir números e letras: "))
    if formato_senha > 3 or formato_senha <= 0:
        print(f"O formato [{formato_senha}] não existe. Operação finalizada.")
    else:
        print("Gerando senha...")
        senha = gerar_senha(formato_senha, n_caracteres)
        print(senha)

