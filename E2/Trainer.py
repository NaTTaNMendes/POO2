class Trainer:
    def __init__(self, name, age, pokemon_list):
        self.name = name
        self.age = age
        self.pokemon_list = pokemon_list

    def describe(self):
        print(f"{self.name} is a trainer who is {self.age} years old and has the following Pokemon:")
        for pokemon in self.pokemon_list:
            print(f"- {pokemon.name}")