#Benjamin Page
#4/9/2019

#Problem 3 - Takes a list of numbers (12,10,32,3,66,17,42,99,20) and prints every other number on a new line.

List = (12,10,32,3,66,17,42,99,20)
x = 0
for y in List:
    if x%2 == 1: #Determines whether a number is even or odd. If odd, the remainder when divided by 2 will always be 1.
        print(List[x])#Prints only odd-numbered items on the list.
    x = x+1 #Continues the next iteration, at the same rate at the for loop so no errors are seen.

