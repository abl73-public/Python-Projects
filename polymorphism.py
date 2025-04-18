#Parent class
class User:
    name = "Mark'
    email = 'mark@gmail.com'
    password = '123abc'
    #Parent class method
    def greeting(self):
        msg = "Hello there!"
        print(msg)

#Child class 1
class Employee(User):
    base_pay = 11.00
    department = 'General'
    #Utilizing polymorphism on the parent class method
    def greeting(self):
        msg = "Hi!"
        print(msg)

#Child class 2
class Customer(User):
    mailing_address = ''
    mailing_list = True
    #Utilizing polymorphism on the parent class method
    def greeting(self):
        msg = "Greetings!"
        print(msg)


