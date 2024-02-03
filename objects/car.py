# object oriented programming

'''an object can be mimiced using programming using 
    attributes - what an object has (height,name,age)
    and methods - what the object does (eat ,sleep,etc.)
     
    class - acts as a blueprint to define what kind of 
          attributes and methods that our object has '''


class Car:


    wheels=4 # class variable - assigned out of the constructor
             # is common for all the objects under the class 
            #this is taken as the default value in case other variable is not declared locally ( eg car_1.wheels=2)

    def __init__(self,make,model,year,color): #called the constructor
        self.make=make      # instance variable
        self.model=model    # instance variable
        self.year=year      # instance variable
        self.color=color    # instance variable

        #each object can have unique values assigned to these instance variables
    def drive(self):                       #method 1
        print('this' ,self.model, 'is driving')
    def stop(self):                        #method 2
        print('this car is stopped')

        pass