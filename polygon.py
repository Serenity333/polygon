#Draws a polygon using a Turtle. Includes Turtle setup
import turtle

t = turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)
        
