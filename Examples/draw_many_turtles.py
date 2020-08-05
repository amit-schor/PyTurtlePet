import arcade
from turtle import Turtle
import numpy as np
w_size = 1920, 1080
arcade.open_window(*w_size,window_title="Drawing Example")
arcade.set_background_color(arcade.csscolor.PALE_GREEN)

arcade.start_render()

# turtle = Turtle(pos=(300,300),size=100)
# turtle.draw()

n_turt_x, n_turt_y = 10,6

for i in range(n_turt_x + 1):
    for j in range(n_turt_y + 1):
        for k in [60,30,10]:
            turtle = Turtle(x=(i*w_size[0]/n_turt_x, j*w_size[1]/n_turt_y), size=k)
            turtle.draw()

arcade.finish_render()
arcade.run()
