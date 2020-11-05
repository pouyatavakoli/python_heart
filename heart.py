#import turtle and time
import turtle
import time
#draw the heart  
for i in range (0,10) :
    n= turtle.Turtle()
    n.color('red')
    n.begin_fill()
    n.fillcolor ('red')
    n.left(140)
    n.forward(180)
    n.circle(-90,200)
    n.setheading (60)
    n.circle(-90,200)
    n.forward (180)
    n.end_fill()
    #write any thing you want between double quotes 
    n.write(".              I hope you are doing great :))")
    time.sleep(.5)
    n.reset()




