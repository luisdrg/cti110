# Luis Rivera Gonzalez
# 3/20/2025
# P4LAB1
# Learning loops using turtle graphics library

import turtle
win = turtle.Screen()
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("triangle")
win.bgcolor('black')

# Draw Triangle
for i in range(3):
    t.forward(300)
    t.left(120)

# Draw Square
side_num = 0
while side_num < 4:
    t.forward(300)
    t.right(90)
    side_num += 1
# end commands
win.mainloop()             # Wait for user to close window