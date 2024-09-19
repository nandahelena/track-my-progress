# Classe que representa um inimigo com atributos de localização e status de vida.
class Inimigo:
    # Atributo de classe para armazenar a quantidade total de inimigos vivos.
    quantidade_vivos: int

    # Inicializa um inimigo com ID, coordenadas e status de vida.
    def __init__(self, id: int, X: int, Y: int, vivo: bool):
        self.id = id          # ID do inimigo.
        self.X = X            # Coordenada X do inimigo.
        self.Y = Y            # Coordenada Y do inimigo.
        self.vivo = vivo      # Status de vida do inimigo (True se estiver vivo, False se estiver morto).

    # Método que atualiza o status do inimigo se ele for atingido pelo lazer na posição (X, Y).
    def foi_acertado(self, X: int, Y: int) -> None:
        # Verifica se a posição do inimigo coincide com a posição do lazer e se o inimigo está vivo.
        if self.X == X and self.Y == Y and self.vivo:
            self.vivo = False          # Marca o inimigo como morto.
            Inimigo.quantidade_vivos -= 1  # Decrementa o número de inimigos vivos.

# Código de execução principal.
if __name__ == "__main__":

    # Lê o número total de inimigos.
    n = int(input())

    # Cria uma lista para armazenar os inimigos.
    inimigos = []
    # Inicializa a quantidade total de inimigos vivos.
    Inimigo.quantidade_vivos = n

    # Lê as informações dos inimigos e cria instâncias da classe Inimigo.
    for id in range(n):
        x, y = map(int, input().split())
        inimigos.append(Inimigo(id, x, y, True))

    # Lê o número de ataques (lazer).
    m = int(input())

    # Processa cada ataque.
    for i in range(m):
        x, y = map(int, input().split())

        # Verifica cada inimigo para ver se foi acertado pelo lazer.
        for inimigo in inimigos:
            inimigo.foi_acertado(x, y)
        
    # Imprime o número de inimigos vivos e mortos.
    print(f"vivos: {Inimigo.quantidade_vivos}")
    print(f"mortos: {n - Inimigo.quantidade_vivos}")
