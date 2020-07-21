"""
By: Jonathan Murphy
Name: PyPaint.py
Date: 7/20/2020
Purpose: Create a chess game using python
"""



from graphics import *

def main():
    win=GraphWin("Paper", 800, 800)
    while(True):
        mouse = win.getMouse()
        brush = Circle(Point(mouse.getX(),mouse.getY()), 10)        
        brush.setFill("blue")
        brush.draw(win)

main()