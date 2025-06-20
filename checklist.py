#list is ordered collection of items.listas are changeable
#my list=[listitem1,listitem2...]
from imdb.linguistics import country

angels=["michael","gabriel","lucifer","raphael"]
print(angels)
#accessing list items:use index
print(angels[0])
print(angels[1])
print(angels[2])
#changing list items
angels[0]="uriel"
angels[2]="azazel"
print(angels)
#looping through the list
for z in angels:
    print(z)
#list methods().append(),insert(),remove(),sort(),pop()
#append()adds an item to the end
angels.append("malek")
print(angels)
#insert()-inserts at position
angels.insert(2,"ezrail")
print(angels)
#remove()-removes an item
angels.remove("azazel")
print(angels)
#sort()-sorts in alphabetical letter
angels.sort()
print(angels)
#pop()-removes last item
angels.pop()
print(angels)
#length()-returns the length
print(len(angels))
#create a list of numbers 30,99...
mynumbers=[7,11,14,17,19,23,26,28,30,33,36,40]
print(mynumbers)
#print numbers greater than 30
for y in mynumbers:
    if y>=40:
        print(y)
        #create a list of countries
        #print the first and last country
        #replace the third country
        #sort list
        countries=["usa","canada","germany","france","spain"]
        print(countries[0])
        print(countries[4])
        countries[2]="belgium"
        print(countries)
        countries.sort()
        print(countries)


