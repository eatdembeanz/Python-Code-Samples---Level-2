#Benjamin Page
#4/9/2019

#Problem 6 -- Creates a list containing 100 random integers between 1 and 1000, then takes the list as a parameter and returns the average.
import random
LongList = []
Total = 0
for i in range(0,100): #For loop runs 100 times, picking a number between 1 and 1,000 each time.
    LongList.append(random.randint(1,1000))
print("List of numbers generated:",LongList)
for x in LongList:
    Total = Total + x
Average = Total / 100
print("Total sum of all numbers:",Total)
print("Average of all numbers:",Average)
