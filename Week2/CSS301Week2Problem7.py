#Benjamin Page
#4/16/2019


#Problem 7 -- Tries to open a file. If that file is not found, throws an exception giving output.
OpenFile = input("Please enter the directory of the file you want to run.")
try:
    open(OpenFile)

except FileNotFoundError:
    raise Exception("Error, file not found.")
print("Success! File can be successfully opened!")
