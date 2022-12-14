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
        for pokemon in self.pokemons:
            print (pokemon)


class Jogador(Personagens):
    tipo = "jogador"

class Oponente(Personagens):
    tipo = "Opnente"

pokemon1 = PokemonEletrico("Pikachu")
pokemon2 = PokemonFogo("Charmander")

jogador1 = Jogador(nome = "Adrian", pokemons = [pokemon1, pokemon2])
jogador1.mostrar_pokemons()
