class Pokemon:
    def __init__(self, especie, level = 1, nome = None):
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

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon_alvo):
        print(f"{self} atacou {pokemon_alvo} com um choque do trovão!")
    
class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon_alvo):
        print(f"{self} atacou {pokemon_alvo} com um ataque fogo!")

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon_alvo):
        print(f"{self} atacou {pokemon_alvo} com um ataque elétrico!")
    
class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon_alvo):
        print(f"{self} atacou {pokemon_alvo} com um ataque de água!")

pokemon1 = PokemonEletrico("Pikachu")
pokemon2 = PokemonFogo("Charmander")
pokemon3 = PokemonAgua("Squartle")

pokemon1.atacar(pokemon2)
pokemon2.atacar(pokemon1)
pokemon3.atacar(pokemon2)

