class Pokemon:
    def __init__(self, name, element_type, level):
        self.name = name
        self.element_type = element_type
        self.level = level

    def attack(self):
        print(f"{self.name} attacks with {self.element_type} power!")

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

    def describe(self):
        print(f"{self.name} is a {self.element_type} type Pokemon at level {self.level}.")