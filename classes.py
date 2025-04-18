
#Activity one
#Main class
class Superhero:
    def __init__(self, name, power, alias):
        self.name = name
        self.power = power
        self.alias = alias

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}. My superpower is {self.power}!")

    def use_power(self):
        print(f"{self.alias} uses {self.power}! 💥")

#Inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, alias, flight_speed):
        super().__init__(name, power, alias)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.alias} is flying at {self.flight_speed} km/h! 🚀")

# Creating a superhero instance
hero1 = FlyingSuperhero("Clark Kent", "Super Strength", "Superman", 3000)
hero1.introduce()
hero1.use_power()
hero1.fly()
