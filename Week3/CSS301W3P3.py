#Benjamin Page
#4/23/2019

#Problem 3-Modifies a recursive tree program.

import turtle
import random
def tree(branchLen,branchSize,t):
    if branchLen > 5:
        if branchLen > 30:
            t.color("brown")
        else:
            t.color("green")
        t.pensize(branchSize)
        t.forward(branchLen)
        randangle = random.randint(15,25)
        randminus = random.randint(10,20)
        t.right(randangle)
        tree(branchLen-randminus,branchSize-2,t)
        t.left(randangle*2)
        tree(branchLen-randminus,branchSize-2,t)
        t.right(randangle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,10,t)
    myWin.exitonclick()


main()
