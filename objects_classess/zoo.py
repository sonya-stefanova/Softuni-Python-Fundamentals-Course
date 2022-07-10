class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name #закачаме името към инстанцията на зоологическата градина
        self.mammals = []
        self.fishes = []
        self.birds = []

    def get_animals_count(self):
        return self.__animals

    # следва да направим два метода ==> функции, а горе са атрубути
    def add_animal(self, species, species_name):
        if species == "mammal":
            self.mammals.append(species_name)
        elif species =="fishes":
            self.fishes.append(species_name)
        elif species == "birds":
            self.fishes.append(species_name)
        self.__animals +=1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species =="fishes":
            return f"Fish in {self.name}: {', '.join(self.fishes)}"
        elif species == "birds":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
n = int(input())
zoo = Zoo(name)


for _ in range(n):
    species, species_name = input().split()
    zoo.add_animal(species, species_name)

searched_species = input()
print(zoo.get_info(searched_species))
print(f"Total animals: {zoo.get_animals_count()}")