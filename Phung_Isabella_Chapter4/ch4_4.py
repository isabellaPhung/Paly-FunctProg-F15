#Isabella Phung
#Period 2
#Project 4.4

from graphics import *
def main():
    win = GraphWin("Interest", 400,600)

    button= Rectangle(Point(100,10), Point(300,70))
    button.draw(win)
    fake = Text(Point(200,40), "Calculate!"). draw(win)
    total1= Text(Point(200,380),"Total: "). draw(win)

 
    
    
    Text(Point(200,100),"Please enter in the Principal!"). draw(win)
    input1= Entry(Point(200,130),10)
    input1.draw(win)



    Text(Point(200,200),"Please enter in the rate!"). draw(win)
    input2= Entry(Point(200,230),10)
    input2.draw(win)


    Text(Point(200,300),"Please enter in the term of the loan!"). draw(win)
    input3= Entry(Point(200,330),10)
    input3.draw(win)

    win.getMouse()
    Principal= eval(input1.getText())
    rate= eval(input2.getText())
    Time= eval(input3.getText())
    
    Interest=Principal*rate*Time

    str(Interest)
    total2= Text(Point(240,380),Interest).draw(win)
    quit.draw(win)
    quit2= Text(Point(200, 550), "Click anywhere to quit!"). draw(win)
    
    win.getMouse()
    win.close()




main()
