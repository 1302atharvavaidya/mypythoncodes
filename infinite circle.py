import turtle 
t=turtle.Turtle()
for i in range(10):
    print(i)
    radius=100-i*10
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()