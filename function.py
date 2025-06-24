#function-a block of code that runs only when it is called
#creating a function
#CALLING A FUNCTION
#def functionname():
#body of function
#CALLING A FUNCTION
#functionname()
def demo():
 print("hello","python is great")
#calling the function
demo()
demo()
demo()
#creating a function
def example():
 print("hello","python is great")
# function with parameter
def greetings(fname):
      print("hello","python is fun",fname)
#calling the function
greetings("Lornegan")
greetings("Maxwell")
#function with multiple parameters
def salutations(name, age):
    print(f"my name is {name} and i am {age} years old")
salutations("Lornegan", 20)
salutations("Maxwell", 25)
salutations("matt", 30)  # Added a valid age argument
# Removed this invalid call as it is incomplete and incorrect
# FUNCTION WITH DEFAULT PARAMETER VALUE
def myfunction(first_name, marks=98):
    print(f"hello {first_name} your marks are {marks}")
# calling the function
myfunction("lornegan,")
myfunction("maxwell", 99)
myfunction("matt", 100)
# function that calculates the area of a rectangle hint a=l*w
def areaofrectangle(l, w):
    return l * w
print("the area of the rectangle is", areaofrectangle(10, 20))
#calling the function
areaofrectangle(10, 20)
#function that calculates the area of a circle(3.14*r*r)
def areaofcircle(r):
    return 3.14 * r * r
print("the area of the circle is", areaofcircle(100))
#calling the function
areaofcircle(100)
#function that calculates the area of a triangle(1/2*b*h)
def areaoftriangle(b, h):
    return 1 / 2 * b * h
print("the area of the triangle is", areaoftriangle(10, 20))
#calling the function
areaoftriangle(10, 20)

