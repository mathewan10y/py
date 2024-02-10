class Car:
    color=None

def changecolor(car,color):
    car.color=color
    print(car.color)

car1=Car()
car2=Car()
car3=Car()

changecolor(car1,'blue')
changecolor(car2,'yellow')
changecolor(car3,'white')
 
class Bike:
    color=None
bike1=Bike()
bike2=Bike()
changecolor(bike1,'red')
