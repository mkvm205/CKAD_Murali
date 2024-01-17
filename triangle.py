import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def main():
    # Set up the turtle
    turtle.speed(1)  # You can adjust the speed (1 is slow, 10 is fast)
    turtle.penup()
    turtle.goto(-50, -50)  # Adjust starting position if needed
    turtle.pendown()

    # Draw a triangle with side length 100
    draw_triangle(100)

    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    main()
