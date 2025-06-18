#operators
#arithmetic operators :+,-,*,/,%,**
x=10
y=20
print("the sum of",x,"and",y,"is",x+y )
print("the difference of",x,"and",y,"is",x-y )
print("the product of",x,"and",y,"is",x*y )
print("the quotient of",x,"and",y,"is",x/y)
print("the remainder of",x,"and",y,"is",x%y)
print("the power of",x,"and",2,"is",x**2)
# COMPARISON OPERATORS:>,<,==,!=,>=,<=
#used to compare values then returns true false
a=40
b=30
#greater than >
print("is",b,"lesser than",a,b<a)
#== equal to
print(f"is {b} equal to {a},?{b==a}")
#less than <
print(f"Is {b} greater than {a},?{b>a}")
#NOT EQUAL TO,!=
print(f"is {b} not equal to {a},?{b!=a}")
#greater than or equal to>=
print(f"is {b} greater than or equal to {a},?{b>=a}")
#less than or equal to
print(f"is {b} lesser than or equal to {a},?{b<=a}")
#logical operators:AND,OR,NOT
#AND-returns true if conditions are true
c=5
print(c>3 and c<10)
print(c>10 and c==5)
#or -returns true if one condition is true
print(c>10 or c==5)
print(c>10 or c>3)
#not returns the reverse
z=True
print(z)
print(not (z))
print(not(c>10))
