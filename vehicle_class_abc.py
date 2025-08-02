
#  Concept: ABC (Abstract Base Classes) in Python force subclasses to implement required methods.

#  Use-case: Define a base Vehicle that can’t be used directly. Only cars, bikes, etc., should be instantiable.


# Importing ABC (Abstract Base Class) and abstractmethod decorator from abc module
from abc import ABC, abstractmethod

# Abstract base class Vehicle
class Vehicle(ABC):
    # Constructor to initialize the name of the vehicle
    def __init__(self, name):
        self.name = name

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def start_engine(self):
        pass

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def stop_engine(self):
        pass

# Concrete subclass Car inheriting from Vehicle
class Car(Vehicle):
    # Implementation of abstract method start_engine
    def start_engine(self):
        print(f"{self.name}'s engine started with key.")

    # Implementation of abstract method stop_engine
    def stop_engine(self):
        print(f"{self.name}'s engine stopped.")

# Concrete subclass Bike inheriting from Vehicle
class Bike(Vehicle):
    # Implementation of abstract method start_engine
    def start_engine(self):
        print(f"{self.name}'s engine started with kick.")

    # Implementation of abstract method stop_engine
    def stop_engine(self):
        print(f"{self.name}'s engine stopped.") 


# ----Testing Code----

# Creating a Car object
my_car = Car("Honda Civic")
my_car.start_engine()                             # Starts car engine
my_car.stop_engine()                              # Stops car engine

# Creating a Bike object
my_bike = Bike("Yamaha FZ")
my_bike.start_engine()                            # Starts bike engine
my_bike.stop_engine()                             # Stops bike engine
