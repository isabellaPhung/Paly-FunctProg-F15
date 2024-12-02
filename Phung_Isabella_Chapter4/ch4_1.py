#Isabella Phung
#Period 2
#Project 4.1

from graphics import *
def main():
    win = GraphWin("Check")
    BrownBorder= Rectangle(Point(0,0), Point(200,200))
    BrownBorder.setFill("Tan3")
    BrownBorder.setOutline("Tan3")
    BrownBorder.draw(win)
    RedBack= Rectangle(Point(10,10), Point(190,190))
    RedBack.setFill("Red3")
    RedBack.setOutline("Red3")
    RedBack.draw(win)


    y=0
    z=0
    for n in range(5):
        MyRect= Rectangle(Point(10,10), Point(25,25))
        MyRect.setFill("Black")
        MyRect.draw(win)
        MyRect.move(0,z)

        Clones=MyRect.clone()

        for i in range(7):
            Clones= Clones.clone()
            Clones.move(33,y)
            Clones.draw(win)
            y=0

        Clones=MyRect.clone()
        Clones.move(-17,16)

        for i in range(5):
            Clones= Clones.clone()
            Clones.move(33,y)
            Clones.draw(win)

        y=y+33
        z=z+33

    #Third row
    MyRect= Rectangle(Point(10,10), Point(25,25))
    MyRect.setFill("Black")
    MyRect.draw(win)
    MyRect.move(0,33)
    Clones= MyRect.clone()
    for i in range(6):
        Clones= Clones.clone()
        Clones.move(33,0)
        Clones.draw(win)

    #Final square
    MyRect= Rectangle(Point(10,175), Point(25,190))
    MyRect.setFill("Black")
    MyRect.draw(win)

    win.getMouse()
main()