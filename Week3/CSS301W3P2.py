#Benjamin Page
#4/23/2019

#Problem 2 -- Iterative and recursive function to reverse a list.
WordList = ["Sunday","Monday","Tuesday"]

def RecurReverse(words):
    return [words[-1]] + RecurReverse(words[:-1]) if words else []


def IterReverse(words):
    if words:
        NewList = []
        ListLen = len(words) -1
        for i in range(ListLen+1):
            NewList.append(words[ListLen])
            ListLen -= 1
        return NewList
    else:
        return []
print("Iterative Reverse List:",IterReverse(WordList))
print("Recursive Reverse List:",RecurReverse(WordList))
