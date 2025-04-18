# Base class
class MovingThing:
    def move(self):
        pass  # Placeholder for subclasses to define their own behavior

# Animal subclasses
class Dog(MovingThing):
    def move(self):
        print("Running 🐕")

class Fish(MovingThing):
    def move(self):
        print("Swimming 🐠")

# Vehicle subclasses
class Car(MovingThing):
    def move(self):
        print("Driving 🚗")

class Plane(MovingThing):
    def move(self):
        print("Flying ✈️")

# Test the classes
things = [Dog(), Fish(), Car(), Plane()]

for thing in things:
    thing.move()
