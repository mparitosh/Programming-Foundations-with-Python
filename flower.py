import turtle

def quad(some_shape):
    some_shape.forward(100)
    some_shape.right(30)
    some_shape.forward(100)
    some_shape.right(150)
    some_shape.forward(100)
    some_shape.right(30)
    some_shape.forward(100)
    some_shape.right(150)

def flowers():
    window=turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(20)
    for i in range(1,73):
        quad(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(300)
    window.exitonclick()
flowers()
