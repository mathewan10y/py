from car import Car

car_1=Car('chevy','corvette','2020','blue') # class object

# 'chevy','corvette',etc== make,model,etc are the attributes of the object 
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

car_2=Car('ford','mustang','2021','red') #class object

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
print(car_2.wheels)

''' 
Car.wheels()=2  --- changes the value of wheels to 2 for both car1 and  car2

car_1.wheels()=2 changes the value of wheels of car1 to 2 whereas the value of car2.wheels remainst ad 4 (which is the default)'''
