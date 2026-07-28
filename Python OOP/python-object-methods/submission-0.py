class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet

        self.hunger -= 1

        print(f'{self.name} has been fed.')
        return

    def printHungerLevel(self):
        print(f'{self.name}{"'"}s hunger level: {self.hunger}')
        return 

# Create a pet
my_pet = Pet("Fluffy")
my_pet.feed()
my_pet.printHungerLevel()
my_pet.feed()
my_pet.printHungerLevel()
my_pet.feed()
my_pet.printHungerLevel()

# TODO: Feed the pet three times
