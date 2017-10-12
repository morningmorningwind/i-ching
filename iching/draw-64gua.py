from PIL import Image, ImageDraw
from numpy import cos, sin, pi
from gua import *

im = Image.new("RGB", (1000, 1000), "white")

n = 64
da = 360.0/float(n)
r = 400.0
a = 0.
for i in range(n):
    arcDeg = a * pi / 180.0
    x, y = (500+r* cos(arcDeg), 500+r * sin(arcDeg))
    b = int2bin(i,nd=6)
    g = B2G[b[:3]]+B2G[b[3:]]
    draw_gua(im, g, length=30, width=5, gap=10, fill=0, center=(x,y), angle=a)
    a += da

# write to stdout
im.save('64gua.png', "PNG")
