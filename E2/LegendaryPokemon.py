from Pokemon import Pokemon

class LegendaryPokemon(Pokemon):
    def __init__(self, name, element_type, level, special_power):
        super().__init__(name, element_type, level)
        self.special_power = special_power

    def use_special_power(self):
        print(f"{self.name} uses its special power: {self.special_power}!")