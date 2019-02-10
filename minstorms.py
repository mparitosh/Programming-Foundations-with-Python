import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    num_turns = 4
    num1_turns = 3
    current_turns = 0
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    while(current_turns<num_turns):
        brad.forward(100)
        brad.right(90)
        current_turns = current_turns + 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    current_turns=0
    
    draco = turtle.Turtle()
    draco.shape("turtle")
    draco.color("white")
    while(current_turns<num1_turns):
        brad.forward(100)
        brad.right(120)
        current_turns = current_turns + 1
    window.exitonclick()
    
draw_square()
