#Benjamin Page

#4/30/2019

#Problem 5-- Extends problem 4 by modifying the object properties, setting a new major.

class Student:
    def __init__(self,name,major):
        self.name = name
        self.major = major
    def greeting(self):
        print("Greetings, "+ self.name + ". Your major is " + self.major)
stud1 = Student("Bill","Computer Sciences")

stud1.greeting()

stud1.major = "Elementary Education"
stud1.greeting()
