# coding: utf-8

import time
import tkinter as tkinter

WIDTH = 900
HEIGHT = 900
LEFT = -2
RIGHT = 0.5
TOP = 1.25
BOTTOM = -1.25
ITERATIONS = 63

root = tkinter.Tk()
image = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
lb1 = tkinter.Label(root, image=image)
lb1.pack()

UPDATE_TIME = 0.01
start_time = time.time()
next_update = start_time + UPDATE_TIME

for y in range(HEIGHT):
    for x in range(WIDTH):
        z = complex(0, 0)
        c = complex(LEFT + x * (RIGHT - LEFT) / WIDTH, TOP + y * (BOTTOM - TOP) / HEIGHT)
        norm = abs(z) ** 2
        for count in range(ITERATIONS):
            if norm <= 4.0:
                z = z * z + c
                norm = abs(z * z)
            else:
                break
        (r, g, b) = (count*4, 0, 0)
        image.put("#%02x%02x%02x" % (r, g, b), (x, y))
        if time.time() > next_update:
            next_update = time.time() + UPDATE_TIME
            root.update()


total_duration = time.time() - start_time
print("duration: %.1fsec, %.1f pixel/sec" %(total_duration, HEIGHT * WIDTH / total_duration))

root.mainloop()
