#python collection\:lists,sets,tuples,dictionary
#dictionary:used to store data in key:value pairs
#key:value
student={
    "name":"Lornegan",
    "age":20,
    "marks":90,
}
print(type(student))
print(student)
#accesing a value
print(student["name"])
#adding new key:value pair
student["country"]="Canada"
print(student["country"])
#updating a value
student["name"]="Michael"
student["age"]=22
student["marks"]=95
student ["country"]="United Kingdom"
print(student)
#print all keys
print(student.keys())
#print all values
print(student.values())
#items()-returns key:values
print(student.items())
#looping through keys and values
for m,n in student.items():
    print(m,n)
#loop through the keys
for m in student.keys():
    print(m)
#loop through the values
for n in student.values():
    print(n)




