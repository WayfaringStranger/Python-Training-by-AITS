''' tk_circles_animate101.py
draw 2 circles via canvas.create_oval(x0, y0, x1, y1, option, ...) 
and animate them using canvas.move() and canvas.after()
'''
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
 
# circle starting center coordinates and radius
CIRCLE_X = 50
CIRCLE_Y = 50
CIRCLE_RADIUS = 50
 
# fix animation rate, time in milliseconds
STEP_TIME = 25  
STEP_X = 1
STEP_Y = 1
 
def move_circle():
    ''' recursive function '''
    canvas.move("orange_circles", STEP_X, STEP_Y)
    x0, y0, x1, y1 = canvas.bbox("orange_circles")
    if x1 > CANVAS_WIDTH: 
        return
    canvas.after(STEP_TIME, move_circle)
   
def circle(x, y, r):
    # form a bounding square using center (x,y) and radius r
    # upper left corner (ulc) and lower right corner (lrc) coordinates of square
    ulc = x-r, y-r
    lrc = x+r, y+r
    # give the circle a tag name for reference
    canvas.create_oval(ulc, lrc, tag="orange_circles", fill='orange')
root = tk.Tk()
root.title("Animated Circle")
# ulc position of rootwindow
root.geometry("+{}+{}".format(150, 80))
# create a canvas to draw on 
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightblue')
canvas.pack()
 
circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS)
circle(CIRCLE_X, CIRCLE_Y-55, CIRCLE_RADIUS/2)
 
move_circle()
 
root.mainloop()
