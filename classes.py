# A class is like a blueprint for creating objects. An object has properties and 
# methods(functions) associated with it. Almost everything in Python is an object

#create a class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I m {self.age}'
    def has_birthday(self):
        self.age += 1

#extend class

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I m {self.age} and my balance is {self.balance}'
#init object
brad = User('Renan','fiborgesrenan@gmail.com', 31)

#init custom object
chica = Customer('Chica', 'chica@email.com', 24)
chica.set_balance(500)

print(chica.greeting())

brad.has_birthday()
print(brad.greeting())
#print(chica.set_balance())