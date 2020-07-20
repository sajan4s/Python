# Class
# Radius, Circumference, area and pi


class Circle():

    # Class variable attribute

    radius = None
    pi = 3.14

    # Function

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius * radius * self.pi


    # Methode

    def circumference(self):

        return self.radius * self.pi * 2



my_circle = Circle(30)

print(my_circle.pi)

print(my_circle.radius)

print(my_circle.area)

print(my_circle.circumference())