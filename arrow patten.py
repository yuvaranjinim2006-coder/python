import turtle

t = turtle.Turtle()
t.speed(5)
t.color("red")

# Draw rose petals
for i in range(36):
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(170)

# Draw stem
t.color("green")
t.right(90)
t.forward(200)

turtle.done()
