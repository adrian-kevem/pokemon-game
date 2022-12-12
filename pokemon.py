class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

pokemon1 = Pokemon("fogo", "charmander")
pokemon2 = Pokemon("elétrico", "pikachu")

print(pokemon1.tipo)
