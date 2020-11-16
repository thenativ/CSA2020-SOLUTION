import turtle
import time

spawn_x = 70
spawn_y = -110
scale = 0.0077

s = turtle.getscreen()
t = turtle.Turtle()
s.bgpic('map.png')
t.down()

for i in range(0,16):
    x = spawn_x
    y = spawn_y
    print("{x}.BIN".format(x=i+1))
    with open("{filename}.BIN".format(filename=str(i+1)), "rb") as f:
        while (movecounter := int.from_bytes(f.read(2), byteorder='big', signed=True)):
            button_press = int.from_bytes(f.read(2), byteorder='big', signed=True)
            x_byte = int.from_bytes(f.read(2), byteorder='big', signed=True)
            y_byte = int.from_bytes(f.read(2), byteorder='big', signed=True)
            dir_x = (1 if x_byte > 0 else -1) if x_byte != 0 else 0
            dir_y = (1 if y_byte > 0 else -1) if y_byte != 0 else 0
            print("{m}: ({x},{y}) | {b}".format(m=movecounter,x=dir_x,y=dir_y,b=button_press))
            for j in range(0, movecounter):
                x += dir_x * scale
                y -= dir_y * scale
            t.goto(x,y)
    time.sleep(2)
input("DONE! Check output")
