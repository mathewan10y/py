'''prevents the user from creating an object of that class
    + compels a user to override the abstract methods in a child class
    
    abstract class -- a class that haves one or more abstract methods
    abstract methods -- a method that has an declaration but does not     have  an implementation'''

from abc import(ABC)
from abc import abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go (self):
        print('the car is moving')
class Motorcycle(Vehicle):
    def go (self):
        print('the bike is moving')

            
# vehicle=Vehicle() doesnt work because vehicle is declared as an abstract class
        
car=Car()
bike=Motorcycle()



