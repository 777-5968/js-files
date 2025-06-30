#oop-object oriented programming
#classes-is a blueprint
#attributes:student class:height,eye colour,skin colour,networth,course
#object-is an instance of a class
class Student:
#constructor method to initialize the attributes
#of each student
    def __init__(self, eye_colour, marks, age, course):
       self.eye_colour=eye_colour
       self .marks=marks
       self.age=age
       self.course=course
#returns a readable string when you print the object
    def __str__(self):
        return f'{self.eye_colour},{self.marks},{self.age},{self.course}'
#a function that displays student age and course
    def display_info(self):
            return f"the student is age {self.age},and is learning {self.course}"
    #a method to return eye colour
    def my_colour(self):
        return f"{self.eye_colour}"
#method to return email
    def get_email(self):
        return f"{self.eye_colour}@phoenix.ac.ke"

#create an object.instance of a class
st1=Student("blue",95,21,"python")
#create another object from instance of a class
st2=Student("green",78,19,"html")
#another object
st3=Student("red",90,22,"javascript")
print(st1)
print(st2)
print(st3)
#calling the display
print(st1.display_info())
print(st2.display_info())
print(st3.display_info())
#calling the eye colour()method
print(st1.my_colour())
print(st2.my_colour())
print(st3.my_colour())
#calling the get_email()method
print(st1.get_email())
print(st2.get_email())
print(st3.get_email())
