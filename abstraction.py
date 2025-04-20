from abc import ABC, abstractmethod

#Create a class that utilizes the concept of abstraction
class gym(ABC):
    #Regular method
    def memberFee(self, amount):
        print("Your monthly dues are: ",amount)
    #Abstract method
    @abstractmethod
    def payment(self, amount):
        pass

#Child class
class DebitorCreditCardPayment(gym):
    #Define the implementation of the parent abstract method
    def payment(self, amount):
        print('Thank you for paying the dues of {} on time. '.format(amount))

#Create an object that utilizes both the parent and child methods
obj = DebitorCreditCardPayment()
obj.memberFee("$150")
obj.payment("$150")
