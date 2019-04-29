#Benjamin Page
#4/23/2019

#Problem 6 Program reads a file and gives a count of occurences for each word.
textD = {}

f = open("testText.txt", "r")

def buildtextD(words):
    for x in words:
        if x not in textD:
            textD[x] = 1
        else:
            textD[x] = textD[x] + 1
            
for line in f:
    w = line.split() #Splits each word by space
    buildtextD(w)
    
print(textD)

f.close()
