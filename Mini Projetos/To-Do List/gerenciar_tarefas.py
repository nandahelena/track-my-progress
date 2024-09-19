import gerenciar_arquivos  # Importa o módulo gerenciar_arquivos para lidar com arquivos

# Função que retorna uma visualização de todas as listas disponíveis
# Usa a função 'retorna_listas' do módulo gerenciar_arquivos
def visualizar_listas():
    return gerenciar_arquivos.retorna_listas()

# Função que lê e exibe o conteúdo de uma lista específica
def ler_lista(nome_lista: str):
    # Abre o arquivo da lista em modo leitura
    with open(f"To-Do List\\Lista de Tarefas\\{nome_lista}", 'r') as archive:
        print("=" * 30)
        print(nome_lista)
        # Percorre o arquivo e exibe as tarefas com seus índices
        for indice, linha in enumerate(archive, start=1):
            print(f"[{indice}°] {linha}")
        print("=" * 30)

# Função que cria uma nova lista de tarefas
# Usa a função 'salvar_arquivo' do módulo gerenciar_arquivos para salvar a lista e a primeira tarefa
def criar_lista(nome_lista: str, tarefa: str):
    return gerenciar_arquivos.salvar_arquivo(nome_lista+'.txt', tarefa)

# Função que adiciona uma nova tarefa a uma lista
def adicionar_tarefa(lista: str, tarefa: str):
    try:
        # Abre a lista em modo leitura para verificar se a tarefa já existe
        with open(f"To-Do List\\Lista de Tarefas\\{lista}", 'r') as archive:
            for linha in archive:
                if linha == tarefa:
                    return ("Esta tarefa já existe. Tente novamente.")
        # Adiciona a tarefa à lista se não existir
        while True:
            with open(f"To-Do List\\Lista de Tarefas\\{lista}", 'a') as archive:
                archive.write(f'\n{tarefa}')  # Adiciona a nova tarefa ao final do arquivo
                ler_lista(lista)
                r = input("Deseja adicionar mais tarefas? (S/N) -> ")
                if r.upper() == "N":  # Encerra a adição de tarefas
                    return False 
                elif r.upper() == "S":  # Continua adicionando mais tarefas
                    return True
        
    except FileNotFoundError:
        print("Houve um erro. Tente novamente.")  # Exibe erro se o arquivo não for encontrado

# Função que remove uma tarefa de uma lista com base no índice fornecido
def marcar_feito(lista: str, indice_tarefa: int):
    while True:
        # Abre a lista e lê todas as linhas
        with open(f"To-Do List\\Lista de Tarefas\\{lista}", 'r') as archive:
            indice_all_tarefas = archive.readlines()
            del indice_all_tarefas[indice_tarefa-1]  # Remove a tarefa com o índice fornecido

        # Reescreve o arquivo sem a tarefa removida
        with open(f"To-Do List\\Lista de Tarefas\\{lista}", 'w') as archive:
            archive.writelines(indice_all_tarefas)

        ler_lista(lista)  # Exibe a lista atualizada
        print("Lista atualizada!")

        # Pergunta se o usuário deseja remover mais tarefas
        r = input("Deseja remover mais tarefas? (S/N) -> ")
        if r.upper() == "N":  # Sai da função se o usuário não quiser remover mais
            return False
        elif r.upper() == "S":  # Continua removendo mais tarefas
            return True
