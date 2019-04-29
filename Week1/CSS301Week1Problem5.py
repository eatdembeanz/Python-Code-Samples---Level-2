#Benjamin Page
#4/9/2019

#Problem 5 -- Takes a list of numbers, and returns a new list with unique elements of the first list.

OldList = [1,3,3,3,6,2,3,5]
NewList = []

for i in OldList:
    if i not in NewList: #If the item in the old list has not already appeared in the new list, adds that item to the new list.
        NewList.append(i)
print(NewList)
