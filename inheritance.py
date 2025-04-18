#parent class
class User:

    name = 'Mark'
    email = 'mark@gmail.com'
    password = '123abc'

#first class inheriting from User
class Employee(User):

    base_pay = 11.00
    department = 'General'

#second class inheriting from User
class Customer (User):

    mailing_address = ''
    mailing_list = True
