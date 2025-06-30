#car:colour,brand,horsepower,speed
class Car:
    def __init__(self,colour, brand, horsepower,speed):
        self.colour =colour
        self.brand= brand
        self.horsepower = horsepower
        self.speed = speed
    def display_info(self):
         return f"this car is a {self.colour} {self.brand} {self.horsepower} {self.speed}"
#create an object
car1=Car("red","Ferrari",1000 , 340)
#creating another object
car2=Car("white","Lamborghini",1200,330)
#calling the display info method
print(car1.display_info())
print(car2.display_info())
#accesing an object attribute
print(car1.colour)
print(car1.horsepower)
print(car2.brand)
print(car2.horsepower)