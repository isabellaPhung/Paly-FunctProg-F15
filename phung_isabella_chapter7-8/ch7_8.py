#Isabella Phung
#Period 2
#Project 7.8
#File: ch7_8.py
#This program creates GUI for user to input trapezoid coordinates and calculates area

from math import *
from graphics import *

#method that checks if trapezoid is actually trapezoid
def validateParallel(x1, y1, x2, y2, x3, y3, x4, y4):
    xdif1= x2-x1
    xdif2= x4-x3
    xdif3= x4-x2
    xdif4= x3-x1

    #to keep the program from having an error when dividing by zero
    if xdif1 == 0:
        xdif1 = 1
    if xdif2== 0:
        xdif2 = 1
    elif xdif3== 0:
        xdif3 = 1
    elif xdif4 == 0:
        xdif4 = 1

    #finds slope
    slope1= (y2-y1)/(xdif1)
    slope2= (y4-y3)/(xdif2)
    slope3= (y4-y2)/(xdif3)
    slope4= (y3-y1)/(xdif4)

    #checks any possibilities of the slopes being the same
    if slope1 == slope2:
        a="ok"
        return a
    elif slope1== slope3:
        a="ok"
        return a
    elif slope1 == slope4:
        a="ok"
        return a
    elif slope2== slope3:
        a="ok"
        return a
    elif slope2==slope4:
        a="ok"
        return a
    elif slope3==slope4:
        a="ok"
        return a
    else:
        a= "invalid"
        return a

def main():
    try:
        win = GraphWin("Trapezoid", 400, 500)

        #rectangle around instructions
        boxbox1= Rectangle(Point(50,10), Point(350,70)). draw(win)
        #instruction text
        instructions = Text(Point(200,40), "Enter in the verticies of your trapezoid!"). draw(win)

        #fake calculate button
        boxbox2= Rectangle(Point(250,180), Point(350,220)). draw(win)
        calculate= Text(Point(300, 200), "Calculate").draw(win)

        #area section
        boxbox3= Rectangle(Point(260, 255), Point(340, 295)). draw(win)
        area= Text(Point(300, 275), "Area"). draw(win)
        #total section
        boxbox4= Rectangle(Point(260, 300), Point(340,340)).draw(win)


        #text for each point
        x1= Text(Point(50, 100), "x1"). draw(win)
        x2= Text(Point(50, 200), "x2"). draw(win)
        x3= Text(Point(50, 300), "x3"). draw(win)
        x4= Text(Point(50, 400), "x4"). draw(win)
        y1= Text(Point(150, 100), "y1"). draw(win)
        y2= Text(Point(150, 200), "y2"). draw(win)
        y3= Text(Point(150, 300), "y3"). draw(win)
        y4= Text(Point(150, 400), "y4"). draw(win)

        #rectangles around text
        box1= Rectangle(Point(30, 80), Point(70, 120))
        for i in range(4):
            boxclone=box1.clone()
            boxclone.draw(win)
            box1.move(0,100)

        box5= Rectangle(Point(130,80), Point(170,120))
        for i in range(4):
            boxclone2=box5.clone()
            boxclone2.draw(win)
            box5.move(0,100)

        #input boxes
        input1= Entry(Point(100,100),5)
        input1. draw(win)
        input2= Entry(Point(100,200),5)
        input2.draw(win)
        input3= Entry(Point(100,300),5)
        input3. draw(win)
        input4= Entry(Point(100,400),5)
        input4. draw(win)
        input5= Entry(Point(200,100),5)
        input5. draw(win)
        input6= Entry(Point(200,200),5)
        input6. draw(win)
        input7= Entry(Point(200,300),5)
        input7. draw(win)
        input8= Entry(Point(200,400),5)
        input8. draw(win)

        #waits for user to click fake button before getting text
        win.getMouse()
        #gets text and assigns to value
        p1x=eval(input1.getText())
        p2x=eval(input2.getText())
        p3x=eval(input3.getText())
        p4x=eval(input4.getText())
        p1y=eval(input5.getText())
        p2y=eval(input6.getText())
        p3y=eval(input7.getText())
        p4y=eval(input8.getText())

        #initiates method to check if correct
        a= validateParallel(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y)
        #if trapezoid is actually trapezoid then calculations are initiated
        if a=="ok":
            #calculates sides
            a=sqrt((p2x-p1x)**2+(p2y-p1y)**2)
            c=sqrt((p1x-p3x)**2+(p1y-p3y)**2)
            b=sqrt((p4x-p3x)**2+(p4y-p3y)**2)
            d=sqrt((p2x-p4x)**2+(p2y-p4y)**2)
            #finds bottom part of right triangle necessary to find height
            e= p3x-p1x
            #finds height
            h=sqrt(c**2-e**2)
            area= h*(a+b)/2
            #finds area using height
            area=round(area)
            #rounds it
            total= Text(Point(300,320),area).draw(win)
            #prints total
            win.getMouse()
        else:
            #if trapezoid is invalid then message printed
            invalid=Text(Point(200,450), "Invalid input. Please click to exit").draw(win)
            win.getMouse()
            win.close()



    #if user didn't type in all necessary numbers
    except NameError:
        booboo1=Text(Point(200,450), "You didn't type in the necessary numbers! Please click to exit!").draw(win)
        win.getMouse()
        win.close()
    #if user didn't type in numbers as values
    except TypeError:
        booboo2=Text(Point(200,450), "You didn't type in numbers! Please click to exit!").draw(win)
        win.getMouse()
        win.close()
    #if user didn't type in correct format
    except SyntaxError:
        booboo3=Text(Point(200,450), "You didn't type it in the right format! Please click to exit!").draw(win)
        win.getMouse()
        win.close()
    #when any unknown errors occur
    except:
        booboo4=Text(Point(200,450), "Sorry! Something didn't work out! Please click to exit!").draw(win)
        win.getMouse()
        win.close()
main()
