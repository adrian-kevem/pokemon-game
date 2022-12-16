from pokemons import *

class Personagens:
    def __init__ (self, nome = None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"
        
        self.pokemons = pokemons

    def __str__ (self):
        return (self.nome)
    
    def mostrar_pokemons(self):
        if self.pkemons:
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("Você ainda não possui nenhum pokemon!")


class Jogador(Personagens):
    tipo = "jogador"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon} capturado!")

class Oponente(Personagens):
    tipo = "Oponente"

pokemon1 = PokemonEletrico("Pikachu")
pokemon2 = PokemonFogo("Charmander")

jogador1 = Jogador(nome = "Adrian", pokemons = [pokemon1, pokemon2])


pokemon_selvagem = PokemonAgua("Blastoise")
print(f"Um pokemon selvagem apareceu! Se trata de um {pokemon_selvagem}!")
jogador1.capturar(pokemon_selvagem)
jogador1.mostrar_pokemons()