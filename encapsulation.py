#Create a class that uses encapsulation
class Protected:
    def __init__(self):
        #Protected attribute
        self._protectedVar = 0
        #Private attribute
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
        
#Create an object of the class
obj = Protected()
#Make use of the protected attribute
print(obj._protectedVar)
obj._protectedVar = 34
print(obj._protectedVar)
#Make use of the private attribute
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
