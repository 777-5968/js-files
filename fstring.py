"f-string"
fname="Ankit"
course="Python"
print(f"Hello {fname} I am learning {course}")
message="hello how you doin'"
#string methods.upper(),lower().\
print(message)
print(message.upper())#converts to uppercase
print(message.lower())#converts to lowercase
print(message.title())
#replace(old,new)
print(message.replace("how","what"))
#find()-findS the index OD SUBSTRING
myfav="Python is interesting"
print(myfav.find("python"))
print(myfav.find("is"))
#SLICING/Substring-substring is a part of a string
#string[start:stop]
text="hello world"
msg="hello"
print(text[0:4])
print(msg[0:2])
print(text[2:])#prints llo
print(text[:5])#slice from beginning to 3
#skip characters
#stop
print(text[::2])
courses=["Javascript"]
#Java
#ript
#script
#escape characters \n\t
print("this is a message \n this goes to a new line")
print("name\t:Age")
print("I send \"greetings to you\"")
print("Caesar sends \"greetings to you\"")
print('it\'s a "string')
print('Archimedes shouted "eureka"')
#"everyone should learn to code"Alexander the great
#he said "I am learning html"
#"It's a new dawn in our empire"Caesar said
print("I am learning \"Python\"")
print('"my men are the bravest ever" Caesar said')
print("Alexander says \"peace unto all nations\"")
print("Alexander is the greatest conqueror of all history")
