#Benjamin Page
#4/9/2019

#Problem 8 -- Count how many words in a list have a length of 4 characters.

WordList = []
FourCount = 0

ListFinished = False
while ListFinished != True:
    WordList.append(input("Enter any word of your choosing."))
    Finish = input("Finish the list?")#As long as the user doesn't input any variation of 'yes' here, repeats the loop.
    if Finish == "yes" or Finish == "Yes" or Finish == "Y" or Finish == "y":
        ListFinished = True


for i in WordList:
    if len(i) == 4: #Checks how many letters are in the word. If it has four letters in it, adds one to a running tally.
        FourCount = FourCount + 1

print("Number of words that have exactly four letters in your list:", FourCount)
