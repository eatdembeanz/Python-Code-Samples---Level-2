#Benjamin Page
#4/23/2019

#Problem 1 -- Iterative and recursive functions to compute the factorial of a given number.

def IterFac(number):
    factor = 1
    if number <1:
        return 1
    while number >1:
       factor *= number
       number = number-1
    return factor



def RecurFac(number):
    if number <1:
        return 1
    else:
        return number * RecurFac(number-1)

print(IterFac(5))
print(RecurFac(5))
