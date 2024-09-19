import os

# Define o caminho para o diretório que vai armazenar os arquivos .txt das listas de tarefas
# Verifica se o diretório já existe. Se não existir, cria o diretório
diretorio = "To-Do List\\Lista de Tarefas"
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Função que salva o conteúdo (tarefas) em um arquivo .txt
def salvar_arquivo(nome_arquivo: str, conteudo: str):
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)  # Gera o caminho completo do arquivo
    with open(caminho_arquivo, "w") as arquivo:  # Abre o arquivo no modo de escrita (overwrite)
        arquivo.write(conteudo)  # Escreve o conteúdo no arquivo

# Função que retorna e exibe todas as listas de tarefas salvas no diretório
def retorna_listas() -> str:
    listas = [arquivo for arquivo in os.listdir("To-Do List\\Lista de Tarefas")]  # Lista todos os arquivos no diretório
    for indice, nome in enumerate(listas, start=1):  # Enumera os arquivos a partir de 1
        print(f"{[indice]} {nome}")  # Exibe os arquivos com índices

# Função que verifica se um arquivo específico (lista) existe no diretório
def arquivo_existe(nome_arquivo: str) -> bool:
    diretorio = "To-Do List\\Lista de Tarefas"
    listas = os.listdir(diretorio)  # Lista todos os arquivos no diretório
    return nome_arquivo in listas  # Retorna True se o arquivo existir, senão False

# Função que verifica se uma linha específica (tarefa) existe dentro de um arquivo (lista)
def linha_arquivo_existe(arquivo: str, linha: str) -> bool:
    try:
        with open(f"To-Do List\\Lista de Tarefas\\{arquivo}", "r") as archive:  # Abre o arquivo no modo de leitura
            return linha in archive  # Retorna True se a linha existir no arquivo, senão False
    except FileNotFoundError:  # Caso o arquivo não seja encontrado, retorna uma mensagem de erro
        return ("A lista selecionada não existe ou não foi digitada corretamente. Tente novamente.")

