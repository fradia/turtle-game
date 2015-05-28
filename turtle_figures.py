"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from swampy.TurtleWorld import *
import math

def square(t,l):
  """This function moves a Turtle t to make a square of length l"""
  fd(t,l)
  for i in range(3):
    rt(t,90)
    fd(t,l)
                
def arc_polygon(t,length,n,k):
  """This function moves a Turtle t to draw the first k edges of an n-polygon. For the function that creates a polygon see Chapter 4
  of Think Python"""
  for i in range(k):
    fd(t, length)
    lt(t,360/n)

    
def arc(t,r,angle):
  """This function move a Turtle t to draw an arc of a given angle and radius r. An alternative for this
  function can be found in Chapter 4 of Think Python."""
  circumference=2*r*math.pi
  n=40
  length=circumference/n
  k=int(angle*n/360)
  # the function arc_polygon is used to draw an approximation of an arc. The number of edges k is computed from the angle parameter
  step_angle = float(angle) / n
  lt(t, step_angle/2)
  # as pointed out in Exercise 4.1 of Chapter 4 of Think Python, making a slight turn on the left reduces the error.
  arc_polygon(t,length,n,k)
  rt(t, step_angle/2)

def flo(t,r):
  """This function moves a Turtle t to draw 4 arcs of 180 degrees which intersect to form a part of a flower.
  The Turtle t draws an arc and it is then rotated of 90 degree before drawing the next arc."""
  arc(t,r,180)
  for i in range(3):
    lt(t,90)
    arc(t,r,180)

def flower(t,r):
  """This function moves a Turtle t to draw a flower of radius r."""
  d1=float(r)
  d2=d1*math.sqrt(2.0)
  flo(t,r)
  # the first part of the flower is created using the function flo.
  pu(t)
  lt(t,45)
  arc(t,d2,45)
  # then the Turtle is moved along an arc of 45 degrees and radius d2. This radius is given by the diagonal
  # of a square of edge d1
  pd(t)
  lt(t,45)
  flo(t,r)
  # the second part of the flower is created using again the function flo.
