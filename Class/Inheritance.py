# Class
# Inheritance


class Animal():

    # Class variable attribute


    # Define

    def __init__(self):
        print("Animal Created")

    # Methode

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")



class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)

        print("Dog Created")

my_animal = Animal()
my_dog = Dog()


print(my_animal)
print(my_animal.who_am_i())
print(my_animal.eat())
print(my_dog)
print(my_dog.eat())