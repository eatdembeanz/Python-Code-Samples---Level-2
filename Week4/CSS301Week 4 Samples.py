class MyClass: #Creates a class labeled MyClass, with a property 'x' set to 5.
    x = 5

p1 = MyClass() #Creates an object named p1.
#print(p1.x) #Prints the value of property 'x' in object 'p1'.


class Person:
#__init__ is used to assign values to any object created in a class.
    def __init__(self,name,age): #Assigns values to name and age.
        self.name = name #Applies the values of whatever's given as 'name' to the same property in 'self'
        self.age = age  #Ditto for 'age'.

p2 = Person("John",36) #Creates an object 'p2' with the class 'Person', and assigns the values of 'name' and 'age.

#print(p2.name) #Prints p2's 'name' value: "John"
#print(p2.age)   #Prints p2's 'age' value: "36"

class Parson: #Creates the class 'Parson'
    def __init__(self,name,age): #Initializes the variables for Parson
        self.name = name #Same as with Person
        self.age = age #Same as with Person
    def myfunc(self): #Defines a function using the properties inside 'self'.
        print("Hello, my name is " + self.name) #Prints the statement, using whatever name is included with 'self'.

p3 = Parson("John",36) #Creates object 'p3', with the values 'John' and '36'
#p3.myfunc() #Will print "Hello, my name is John".

p2.age = 40 #Modifies the age value of object p2, from 36 to 40
#print(p2.age) #Prints the age, now modified. Should be '40'.

del p2.age #Deletes the age property from object p2.
#print(p2.name, p2.age) #Should return 'Person' object has no attribute 'age'.

del p2 #deletes object p2.
print(p2.name) #Should return 'name p2 is not defined'.
print(p2.age)
