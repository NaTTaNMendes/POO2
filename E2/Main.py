from LegendaryPokemon import LegendaryPokemon
from Pokemon import Pokemon
from Trainer import Trainer

pikachu = Pokemon("Pikachu", "Electric", 10)
charmander = Pokemon("Charmander", "Fire", 8)
bulbasaur = Pokemon("Bulbasaur", "Grass", 7)

ash = Trainer("Ash", 10, [pikachu, charmander, bulbasaur])
ash.describe()

mewtwo = LegendaryPokemon("Mewtwo", "Psychic", 50, "Psystrike")
mewtwo.attack()
mewtwo.level_up()
mewtwo.use_special_power()
mewtwo.describe()