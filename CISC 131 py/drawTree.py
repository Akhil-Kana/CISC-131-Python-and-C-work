import turtle

def main():
    pen = turtle.Turtle()
    turtle.Screen().setup(width=800, height=800)
    turtle.Screen().setworldcoordinates(-400, -400, 400, 400)
    turtle.Screen().title("Recursive Tree")
    pen.speed(10)
    pen.color("purple")

    # start the drawing in middle of screen near the bottom
    # and turn pen so it is facing upwards
    pen.up()
    pen.goto(0, -250)
    pen.left(90)

    # draw trunk (which will recursively draw rest of tree)
    drawBranch(pen, 175, 4)

    # keep window open until user closxes it
    turtle.done()

def drawBranch(pen, length, min_length):
    # WRITE CODE HERE
    if length >= min_length:
        pen.down()
        pen.forward(length)
        pen.left(30)
        drawBranch(pen, length//(4/3), min_length)
        


main()
