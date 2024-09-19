# Classe que representa um personagem com atributos de nome, ataque, defesa e vida.
class Personagem:
    def __init__(self, nome: str, ataque: int, defesa: int, vida: int):
        # Inicializa os atributos do personagem.
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida

    # Método que determina se o personagem sobreviveu após receber o golpe.
    def sobreviveu(self, dano: int) -> bool:
        # Calcula o dano efetivo após aplicar a defesa do personagem.
        dano -= self.defesa
        # Atualiza a vida do personagem com base no dano recebido.
        self.vida -= dano
        # Verifica se a vida do personagem caiu para zero ou menos.
        if self.vida <= 0:
            return False  # O personagem morreu.
        else:
            return True   # O personagem sobreviveu.

# Código de execução principal.
if __name__ == "__main__":

    # Lê os atributos do personagem a partir da entrada do usuário.
    nome = input("Nome do personagem: ")
    ataque = int(input("Ataque do personagem: "))
    defesa = int(input("Defesa do personagem: "))
    vida = int(input("Vida do personagem: "))

    # Cria uma instância do personagem com os atributos fornecidos.
    personagem = Personagem(nome, ataque, defesa, vida)

    # Lê o valor do dano recebido pelo personagem.
    dano = int(input("Dano recebido: "))

    # Verifica se o personagem sobreviveu ao dano recebido e imprime o resultado.
    if personagem.sobreviveu(dano):
        print(f"{personagem.nome} sobreviveu!!!")
    else:
        print(f"{personagem.nome} morreu :(")
