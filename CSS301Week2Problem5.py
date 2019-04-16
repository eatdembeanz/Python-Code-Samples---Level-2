#Benjamin Page
#4/16/2019

#Counts the number of times each letter appears in a given string.

def LetterCounter(word):
    WordDict = {}
    for x in word:
        print(x)
        if x in WordDict:
            y = y+1
            WordDict[x] = y
        if x not in WordDict:
            y = 1
            WordDict[x] = y
            

    print(WordDict)
    pass

new_word = input("Enter a string of letters.")
LetterCounter(new_word)
