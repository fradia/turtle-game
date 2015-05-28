"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from swampy.TurtleWorld import *
import math
import turtle_figures
# the module turtle_figures is imported

def forward(t,l):
    """This function defines a movement forward of length l by a turtle t. The turle has a pen and the functions 
    pu and pd stand for "pen up" and
    "pen down" respectively. The turtle t starts with the pen up and does not leave a trace"""

    pu(t)
    fd(t,l)
    pd(t)
    
def backward(t,l):
    pu(t)
    bk(t,l)
    pd(t)
    
def rightward(t,l):
    """The turtle t starts with the pen up and it is rotated on the right of 90 degrees with the function rt"""
    
    pu(t)
    rt(t,90)
    fd(t,l)
    pd(t)
    
def leftward(t,l):
    pu(t)
    lt(t,90)
    fd(t,l)
    pd(t)

world=TurtleWorld()
ugo=Turtle()
lt(ugo,90)
ugo.delay=0.01
"""An instance of the class Turtle is created and given the name ugo. ugo is rotated on the left of 90 degrees.
To make ugo faster a delay of 0.01 is given"""

button=raw_input('Hi! This is Ugo, the turtle\n'
'Press f,distance to move Ugo forward of a given distance (for example f,100)\n'
'Press b,distance to move Ugo forward of a given distance (for example b100)\n'
'Press r,distance to move Ugo rightward of a given distance (for example r,40)\n'
'Press l,distance to move Ugo leftward of a given distance (for example l,80)\n'
'Press square,edge if you want Ugo to draw a square of given edge (for example square,35)\n'
'Press circle,radius if you want Ugo to draw a circle of a given radius (for example circle,50)\n'
'Press flower,raidus if you want Ugo to draw a flower of a given radius (for example flower,100)\n'
'Press q if you want to quit the game\n')
"""Instructions are given to the user"""

x=[w for w in button.split(',')]
while button != 'q':
    if x[0]=='f':
        forward(ugo,int(x[1]))
    elif x[0]=='b':
        backward(ugo,int(x[1]))
    elif x[0]=='r':
        rightward(ugo,int(x[1]))   
    elif x[0]=='l':   
        leftward(ugo,int(x[1]))
    elif x[0]=='square':
        turtle_figures.square(ugo,int(x[1]))
    elif x[0]=='flower':
        turtle_figures.flower(ugo,int(x[1]))
    elif x[0]=='circle':
        turtle_figures.arc(ugo,int(x[1]),360)    
    button=raw_input()
    x=[w for w in button.split(',')]
exit()
