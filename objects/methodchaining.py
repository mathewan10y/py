''' method chaining -- calling multiple methods sequentially 
                        each call performs an acton on the same object and returns self'''


class Car:

    def turnon(self):
        print('the engine is started')    # we have to return(self) where
        return(self)                       # method chaining is used
    def drive(self):        
        print('you are driving the car')
        return(self)
    def brake(self):
        print('you stopped the car')
        return(self)
    def turnoff(self):
        print('you turned off the engine')
        return(self)
    
car = Car()
car.turnon().drive()    # command for method chaining

car.brake().turnoff()