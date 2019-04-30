#Benjamin Page
#4/16/2019

#Problem 2 -- Creates a dictionary where the keys are numbers ranging from 1 to 20 and the values are cubes of the keys. Then prints the dictionary.

TwentyDict = {}
for i in range(1,21):
    icube = i*i*i
    TwentyDict.update({i : icube})
print(TwentyDict)
