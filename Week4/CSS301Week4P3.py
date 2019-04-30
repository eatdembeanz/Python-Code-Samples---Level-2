#Benjamin Page
#4/30/2019

#Problem 3-- Uses __init__() to assign values for name and major in the class "Student"

class Student:
    def __init__(self,name,major):
        self.name = name
        self.major = major

stud1 = Student("Bill","Computer Sciences")
print(stud1.name,stud1.major)
