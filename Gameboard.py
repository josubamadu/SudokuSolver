import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import numpy as np
import Solver
import TestBoards

squareSideLength = 50
windowWidth=9*squareSideLength
windowHeight=9*squareSideLength
numberOfRows = 9
numberOfColumns = 9
counter = 0


def update(c):
    for x in range(numberOfRows):
        for y in range(numberOfColumns):
            x0 = x * squareSideLength
            y0 = y * squareSideLength
            x1 = x0 + squareSideLength
            y1 = y0 + squareSideLength
            if hist[c][y][x] != None:
                t = hist[c][y][x]
            else:
                t = ""
            centerVal = squareSideLength/2
            canvas_1.create_rectangle(x0,y0,x1,y1,fill="#fff0ff",activefill="#ffff00")
            canvas_1.create_text(x0+centerVal,y0+centerVal,text=t,width=squareSideLength,fill="#000000",justify="center",font=fontObj)

def next(c,max):
    global counter
    counter = c + 1
    if counter == max:
        counter = c
    update(counter)

def prev(c):
    global counter
    counter = c - 1
    if counter < 0:
        counter = 0
    update(counter)

### Main Function ###

window = tk.Tk()
window.geometry(str(windowWidth+squareSideLength)+"x"+str(windowHeight+squareSideLength))
window.title("Gameboard")
fontObj = tkFont.Font(size=18)

#hist = Solver.Solver(TestBoards.PracticeGameEasy)
#hist = Solver.Solver(TestBoards.PracticeGameMedium)
hist = Solver.Solver(TestBoards.PracticeGameHard)
#print(hist)
canvas_1 = tk.Canvas(window,width=windowWidth,height=windowHeight)
canvas_1.pack()
update(0)

nextButton = tk.Button(window,text="Next",command=lambda: next(counter,len(hist)))
previousButton = tk.Button(window,text="Previous",command=lambda: prev(counter))

nextButton.pack()
previousButton.pack()
canvas_1.pack()
window.mainloop()