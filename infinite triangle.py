import turtle 
t=turtle.Turtle()
for i in range(10):
    print(i)
    
    l= 300-i*22.36
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.penup()
    t.goto(10+i*11.18, 5+i*11.18)
    t.left(120)
    t.pendown()