#Isabella Phung
#Period 2
#Project 4.3

from graphics import *
def main():
    win=GraphWin("dice", 800, 210)
    outside= Rectangle(Point(20,40), Point(140,160))
    outside.draw(win)

    dot=Circle(Point(80,100),10)
    dot.setFill("Black")
    dot.draw(win)


    Clone= outside.clone()
    for i in range(5):
        Clone= Clone.clone()
        Clone.move(130,0)
        Clone.draw(win)

    _1_=dot.clone()
    mid= _1_.clone()
    _1_.move(90,-40)
    _3_=_1_.clone()
    _3_.move(80,80)
    _3_.draw(win)
    _2_= _1_.clone()
    _2_.move(340,0)
    _4_= _1_.clone()
    _4_.move(130,80)


    _1_.draw(win)
    for n in range(4):
        _1_=_1_.clone()
        _1_.move(130,0)
        _1_.draw(win)

    for u in range(4):
        _3_=_3_.clone()
        _3_.move(130,0)
        _3_.draw(win)

    _2_.draw(win)
    for d in range(2):
        _2_=_2_.clone()
        _2_.move(130,0)
        _2_.draw(win)

    for t in range(2):
        mid= mid.clone()
        mid.move(260,0)
        mid.draw(win)

    for b in range(3):
        _4_=_4_.clone()
        _4_.move(130,0)
        _4_.draw(win)

    _5_= _1_.clone()
    _5_.move(0, 40)
    _5_.draw(win)
    _5_=_5_.clone()
    _5_.move(80,0)
    _5_.draw(win)



    win.getMouse()
main()