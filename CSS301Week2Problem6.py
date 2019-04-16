#Benjamin Page
#4/16/2019

#Asks the user for a number and throws an error using 'raise' if input is greater than 20.



Number = input("Please enter a number")

try:
    int(Number)

except ValueError:
    raise Exception("Error, please enter a number.")
num = int(Number)
if num > 20:
    raise Exception("Error. Number is greater than 20.")
else:
    print(num)
