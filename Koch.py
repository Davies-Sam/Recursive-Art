import turtle

#make the turtle start at the middle left of the screen
wn = turtle.Screen()
w = wn.window_width()
h = wn.window_height()
t = turtle.Turtle()
t.speed(100)
t.up()
t.ht()
t.goto(- w /2, 0)
t.st()
t.down()
depth = 5

start = "f"

for i in range(depth):
    start = start.replace("f", "f+f--f+f")

def main():
    for char in start:
        if char == 'f':
            t.forward(2)
        elif char == '+':
            t.left(60)
        elif char == '-':
            t.right(60)
    turtle.done()

if __name__ == "__main__":
    main()


