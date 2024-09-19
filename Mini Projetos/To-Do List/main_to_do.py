import gerenciar_tarefas  # Importa o módulo responsável por gerenciar tarefas
import gerenciar_arquivos  # Importa o módulo responsável por gerenciar arquivos

# Função que solicita e valida um número inteiro digitado pelo usuário
def solicita_inteiro(prompt: str) -> int:
    while True:  # Loop contínuo até uma entrada válida ser fornecida
        try:
            return int(input(prompt))  # Tenta converter o input em um inteiro
        except ValueError:  # Se a conversão falhar, o usuário é informado e solicitado a tentar novamente
            print("Insira um número válido, ou [3] para sair.")

# Função que verifica se uma string é válida, ou seja, se contém mais de 0 caracteres
def is_string_valida(string: str) -> bool:
    return True if len(string) > 0 else False  # Retorna True se o comprimento da string for maior que 0, senão False

# Função que garante que o nome de uma lista termine com ".txt"
# Caso o usuário insira um nome sem a extensão ".txt", ela é automaticamente adicionada
def formata_nome_lista(input_lista: str) -> str:
    return input_lista if input_lista.endswith(".txt") else input_lista+".txt"  # Adiciona ".txt" ao final, se necessário

# Função que cria uma nova lista de tarefas
# Ela valida o nome da lista e da primeira tarefa antes de prosseguir com a criação
def criar_lista():
    print("[1] Criar lista de tarefas selecionado. Vamos prosseguir!")

    # Solicita o nome da lista e da primeira tarefa que será adicionada à lista
    nome_lista = input("Insira o nome da sua lista: ")
    primeira_tarefa = input(f"Insira a 1° tarefa da lista {nome_lista}: ")

    # Verifica se o nome da lista e a primeira tarefa são válidos
    if is_string_valida(primeira_tarefa) and is_string_valida(nome_lista):
        # Se forem válidos, chama a função para criar a lista no módulo gerenciar_tarefas
        gerenciar_tarefas.criar_lista(nome_lista, primeira_tarefa)
        print("Lista criada!")

    # Se o nome da lista ou a tarefa forem inválidos, exibe uma mensagem de erro
    else:
        print("O nome da lista e/ou sua tarefa precisam ser nomeados com no mínimo 1 caractere. Tente novamente.")

# Função principal que exibe o menu e gerencia a interação do usuário
def main():
    # Exibe o cabeçalho da aplicação
    print("--------------------")
    print("     To-Do List!    ")
    print("--------------------")

    # Exibe as opções do menu para o usuário
    print("[1] Criar nova lista de tarefas")
    print("[2] Visualizar listas de tarefas")
    print("[3] Sair")

    # Solicita que o usuário insira um número correspondente à sua escolha
    comando = solicita_inteiro("Insira um dígito -> ")

    # Valida se o número inserido é uma opção válida
    if comando <= 0 or comando >= 4:
        print(f"Ação solicitada de número [{comando}] não existe. Tente novamente.")
    
    # Se o usuário escolher [1], chama a função criar_lista para criar uma nova lista
    elif comando == 1:
        criar_lista()
        return main()  # Retorna ao menu principal após criar a lista
    
    # Se o usuário escolher [2], exibe as listas existentes para visualização
    elif comando == 2:
        print("=" * 30)
        gerenciar_tarefas.visualizar_listas()  # Exibe as listas disponíveis

        # Solicita ao usuário o nome da lista que deseja visualizar
        nome_lista = input("Digite o nome da lista que deseja visualizar: ")
        nome_lista = formata_nome_lista(nome_lista)  # Formata o nome da lista para garantir que termine com ".txt"
        
        # Verifica se a lista existe
        if gerenciar_arquivos.arquivo_existe(nome_lista):
            # Se o arquivo existir, lê e exibe a lista de tarefas
            gerenciar_tarefas.ler_lista(nome_lista)

            # Exibe as opções para interagir com a lista
            print("[1] Adicionar itens [2] Riscar itens [3] Sair" )
            comando = int(input("Insira um número -> "))

            # Loop contínuo para permitir interações repetidas com a lista
            while True:
                if comando == 3:
                    return  # Sai do loop e da função se o usuário escolher sair
                
                elif comando == 1:  # Adiciona uma nova tarefa à lista
                    tarefa_nova = input("Insira a tarefa -> ")
                    if gerenciar_tarefas.adicionar_tarefa(nome_lista, tarefa_nova) == False:
                        return main()  # Se a adição falhar, retorna ao menu principal
                    
                elif comando == 2:  # Risca ou remove uma tarefa da lista
                    indice_tarefa = int(input("Insira o índice (N°) da tarefa que deseja excluir -> "))
                    if gerenciar_tarefas.marcar_feito(nome_lista, indice_tarefa) == False:
                        return main()  # Se a remoção falhar, retorna ao menu principal
                
                else:
                    # Se o comando for inválido, exibe uma mensagem de erro e repete o loop
                    print("Essa lista não existe. Tente novamente ou digite [1] para sair.")
        else:
            # Se a lista não for encontrada, exibe uma mensagem de erro e retorna ao menu principal
            print(" >>> A lista selecionada não existe ou foi digitada incorretamente. Redirecionando ao menu.")
            return main()

if __name__ == "__main__":
    main()  # Chama a função principal
