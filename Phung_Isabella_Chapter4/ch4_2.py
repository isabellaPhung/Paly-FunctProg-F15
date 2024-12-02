#Isabella Phung
#Period 2
#Project 4.2

from graphics import *
def main():
    win= GraphWin("WhichWitchisWhich",600,600)
    hair= Polygon(Point(150,50), Point(75,290), Point(225,290))
    hair.setFill("Black")
    hair.draw(win)
    hat= Polygon(Point(150,10), Point(100, 200), Point(200,200))
    hat.setFill("Black")
    hat.draw(win)
    face= Oval(Point(100,160), Point(200, 300))
    face.setFill("Green")
    face.draw(win)
    lip=Circle(Point(150,230), 40)
    lip.setFill("Green")
    mouth=lip.clone()
    mouth.setFill("red3")
    mouth.move(0,10)
    mouth.draw(win)
    lip.draw(win)
    leftcheek= Circle(Point(110,230),25)
    leftcheek.setFill("Green")
    leftcheek.draw(win)
    rightcheek= leftcheek.clone()
    rightcheek.move(80,0)
    rightcheek.draw(win)
    nose= Oval(Point(130,200), Point(170, 260))
    nose.setFill("Green")
    nose.draw(win)
    hatbrim= Oval(Point(75, 155),Point(225,220))
    hatbrim.setFill("Black")
    hatbrim.draw(win)

    stem=Rectangle(Point(420,375),Point(430,490))
    stem.setFill("Green4")
    stem.draw(win)
    _1_= Oval(Point(350,400), Point(500,500))
    _1_.setFill("Orange")
    _2_=_1_.clone()
    _2_.move(-20,0)
    _2_.draw(win)
    _3_=_1_.clone()
    _3_.move(20,0)
    _3_.draw(win)
    _1_.draw(win)
    _4_= Oval(Point(400,400), Point(450,500))
    _4_.draw(win)




    win.getMouse()


main()