#Draws a polygon using a Turtle. WARNING: Does NOT include Turtle setup

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
