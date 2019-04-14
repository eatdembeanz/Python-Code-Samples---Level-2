#Benjamin Page
#4/9/2019

#Problem 7 -- Sum up all positive even numbers in a list, and subtract all negative odd numbers from the same list.
ListFinished = False
BigList = []
while ListFinished != True:
    BigList.append(int(input("Enter a number, either positive or negative.")))
    FinishQuestion = input("Finish the list?") #As long as the user doesn't put in any variation of 'yes', repeats the loop.
    if FinishQuestion == "yes" or FinishQuestion == "Yes" or FinishQuestion == "Y" or FinishQuestion == "y":
        ListFinished = True
PosEvenSum = 0
NegOddDif = 0
for i in BigList:
    if i > 0:
        if i%2 == 0:
            PosEvenSum = PosEvenSum + i #If the value is greater than zero (positive) and divisible by 2 (even), adds it to a running sum.
    else:
        if i%2 == 1:
            NegOddDif = NegOddDif + i #If the value is NOT greater than zero (negative) and NOT divisible by 2 (odd), adds it to a running sum.
print("Sum of all positive numbers:",PosEvenSum)
print("Sum of all negative numbers:",NegOddDif)
print("Sum of positive even numbers minus negative odd numbers:",PosEvenSum + NegOddDif) #Combines both running sums, giving us a total.
