'''inheritance  - the child class inherits every methods,class variables that the parent class has'''

class Animal: 
    alive=True

    def eat(self):                         #method 1
        print('this animal is eating')
    def sleep(self):                       #method 2
        print('this animal is sleeping')

class Rabbit(Animal): #rabbit is the child class of the parent class animal
    pass
    def run(self):
        print('this rabbit is running')

class Fish(Animal):
    def swim(self):
        print('this fish is swimming')
    pass

class Hawk(Animal):
    def fly(self):
        print('this hawk is flying')
    pass

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()        # object

print(rabbit.alive)
rabbit.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()





