#Benjamin Page
#4/9/2019

#Use a for statement to print 10 random numbers between 25 and 50.

import random #Imports the module dedicated to functions that produce randomized values.

for i in range(0,10):#Runs a loop that will go for exactly 10 iterations, then stop.
    print(random.randint(25,50))#Finds a random integer between 25 and 50, then restarts the loop.
