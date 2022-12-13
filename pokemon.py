class Pokemon:
    def __init__(self, tipo, especie, level = 1, nome = None):
        self.tipo = tipo
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return (f"{self.especie} ({self.tipo} - Level {self.level})")

    def atacar(self, pokemon_alvo):
        print(f"{self} atacou {pokemon_alvo}")

pokemon1 = Pokemon("fogo", "charmander", nome = "Gui", level = 50)
pokemon2 = Pokemon("elétrico", "pikachu")

print(pokemon1.tipo)
print(pokemon1.nome)
pokemon1.atacar(pokemon2)
pokemon2.atacar(pokemon1)
