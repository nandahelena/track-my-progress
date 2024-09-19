# Classe que representa um projeto com requisitos de programação e design.
class Projeto:
    def __init__(self, requisito_programacao, requisito_design):
        # Inicializa os requisitos do projeto.
        self.requisito_programacao = requisito_programacao
        self.requisito_design = requisito_design

# Classe base para empregados, com atributos relacionados ao valor por projeto e valor recebido.
class Empregado:
    def __init__(self, valor_por_projeto, valor_recebido):
        # Inicializa o valor que o empregado receberá por projeto e o valor já recebido.
        self.__valor_por_projeto = valor_por_projeto
        self.__valor_recebido = valor_recebido

    # Propriedade para acessar o valor recebido.
    @property
    def valor_recebido(self):
        return self.__valor_recebido

    # Método que indica se o empregado é capaz de entregar um projeto.
    # Por padrão, um empregado normal não é capaz de entregar nenhum projeto.
    def capaz(self, projeto: Projeto) -> bool:
        return False

    # Método para receber a recompensa, ou seja, aumentar o valor recebido pelo valor do projeto.
    def receber_recompensa(self) -> None:
        self.__valor_recebido += self.__valor_por_projeto

# Classe derivada de Empregado que representa um programador.
class Programador(Empregado):
    def __init__(self, valor_por_projeto: int, habilidade_programacao: int):
        # Inicializa o programador com o valor por projeto e a habilidade de programação.
        super().__init__(valor_por_projeto, 0)
        self.__habilidade_programacao = habilidade_programacao

    # Método que verifica se o programador é capaz de entregar o projeto baseado na sua habilidade de programação.
    def capaz(self, projeto: Projeto) -> bool:
        return self.__habilidade_programacao >= projeto.requisito_programacao

# Classe derivada de Empregado que representa um designer.
class Designer(Empregado):
    def __init__(self, valor_por_projeto: int, habilidade_design: int):
        # Inicializa o designer com o valor por projeto e a habilidade de design.
        super().__init__(valor_por_projeto, 0)
        self.__habilidade_design = habilidade_design

    # Método que verifica se o designer é capaz de entregar o projeto baseado na sua habilidade de design.
    def capaz(self, projeto: Projeto) -> bool:
        return self.__habilidade_design >= projeto.requisito_design

# Código de execução principal.
if __name__ == "__main__":

    # Lê o valor por projeto e a habilidade do programador.
    valor, habilidade = map(int, input().split())
    programador = Programador(valor, habilidade)

    # Lê o valor por projeto e a habilidade do designer.
    valor, habilidade = map(int, input().split())
    designer = Designer(valor, habilidade)

    # Lê o número de projetos.
    n = int(input())
    for _ in range(n):
        # Lê os requisitos de programação e design para cada projeto.
        requisito_programacao, requisito_design = map(int, input().split())
        projeto = Projeto(requisito_programacao, requisito_design)

        # Verifica se tanto o programador quanto o designer são capazes de entregar o projeto.
        if programador.capaz(projeto) and designer.capaz(projeto):
            # Se ambos são capazes, eles recebem a recompensa.
            programador.receber_recompensa()
            designer.receber_recompensa()

    # Exibe o valor total recebido por cada um.
    print(f"Programador: R$ {programador.valor_recebido}")
    print(f"Designer: R$ {designer.valor_recebido}")
