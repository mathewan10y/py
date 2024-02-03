'''multi inheritance -- when a derived class(child) derives another derived (child) class'''

class Organisms:

    alive=True

class Animal(Organisms):
        def eat(self):                         #method 1
            print('this animal is eating')
        def sleep(self):                       #method 2
            print('this animal is sleeping')
class Dogs(Animal):
     
     def bark(self):
          print('this dog is barking')
dog=Dogs()
print(dog.alive)

'''case 2'''

class Prey:
    def flee(self):
        print('this animal flees')

class Predator:
    def hunt(self):
        print('this animal hunts')
   
class Rabbit(Prey):
    pass
    
class Fish(Prey,Predator):
    pass
class Lion(Predator):
    pass 
    
lion=Lion()
lion.hunt()