from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 0 ]
for x in range(500):
    color[0] += 10
    if color[0] > 255:
        color[0] = color[0] % 4
    color[1] += 15
    if color[1] > 255:
        color[1] = color[1] % 3
    color[2] += 5
    if color[2] > 255:
        color[2] = color[2] % 2
    #draw_line(250, 250, 500 - x, 500, screen, color)
    draw_line(250, 250, 500 - x, 500, screen, color)
    #draw_line(500, 500 - x, 250, 250, screen, color)
    #draw_line(500, 500 - x, 250, 250, screen, color)
    draw_line(250, x, 500 - x, 500, screen, color)
    #draw_line(x, x, 500 - x, 500, screen, color)
    draw_line(x, 500 - x, 250, x, screen, color)
    draw_line(x, 500 - x, 250, 250, screen, color)
display(screen)
save_extension(screen, 'img.png')
