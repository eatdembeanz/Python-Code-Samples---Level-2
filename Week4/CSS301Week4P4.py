#Benjamin Page

#4/30/2019

#Problem 4-- Extends Student class by creating a method that prints a greeting using the student's name and executing it on the student1 object.

class Student:
    def __init__(self,name,major):
        self.name = name
        self.major = major
    def greeting(self):
        print("Greetings, "+ self.name)
stud1 = Student("Bill","Computer Sciences")

stud1.greeting()
