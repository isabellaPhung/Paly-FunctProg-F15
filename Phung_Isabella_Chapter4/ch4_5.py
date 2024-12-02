#Isabella Phung
#Period 2
#Project 4.5

from graphics import *
def main():
    win= GraphWin("distance",400,400)
    message= Text(Point(200,40),"Click to make the first point!"). draw(win)
    p1= win.getMouse()
    p1.draw(win)
    p2= win.getMouse()
    p2.draw(win)
    line= Line(p1, p2)
    line.draw(win)


    win.getMouse()
main()