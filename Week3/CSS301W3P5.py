#Benjamin Page
#4/23/2019

#Problem 5 -- Uses a recursive function to compute the first 100 values of the Fibonacci sequence, and writes them to a file.

def recurfibo(n):
    if n == 1:
        return 0
    elif n == 0:
        return 1
    else:
        return recurfibo(n-1) + recurfibo(n-2)


outfile = open("FibonacciList.txt","w")
for i in range(1,100):
    Fibonumber = str(recurfibo(i))
    print("Step ", i, ": ", Fibonumber)
    currentnumber = str(i)
    outfile.write("Fibonacci Number Step " + currentnumber + ":" + Fibonumber + '\n')

outfile.close()
