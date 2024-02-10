''' super() -- is a function used to give access to the methods of a parent class. it returns a temporary objecet of a parent class when used'''


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width


class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print(self.length*self.width)
        
        pass
class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height
    def volume(self):
        print(self.length * self.width * self.height)

square1=Square(2,2)  #object1
rect1=Rectangle(3,4) #object2
cube1=Cube(3,3,3)    #object3

print(square1.length,rect1.width,cube1.height,sep='\n')
square1.area()
cube1.volume()