from PIL import Image, ImageDraw
from numpy import cos, sin, pi
from gua import *

im = Image.new("RGB", (1000, 1000), "white")

n = 8
da = 360.0/float(n)

# outer
r1 = 400.0
a = 0.
for i in range(n):
    arcDeg = a * pi / 180.0
    x, y = (500+r1* cos(arcDeg), 500+r1 * sin(arcDeg))
    b = int2bin(i,nd=3)
    g = B2G[b]
    draw_gua(im, g, length=150, width=10, gap=40, fill=0, center=(x,y), angle=a)
    a += da
    
# inner
r2 = 250.0
a = 0.
for i in range(n):
    arcDeg = a * pi / 180.0
    x, y = (500+r2* cos(arcDeg), 500+r2 * sin(arcDeg))
    b = int2bin(i,nd=3)
    g = B2G[b]
    draw_gua(im, g, length=150, width=10, gap=40, fill=0, center=(x,y), angle=a)
    a += da

# circle:

draw = ImageDraw.Draw(im)
r = 0.5*(r1+r2)

draw.arc([500-r,500-r,500+r,500+r],0,360,fill=128)

# write to stdout
im.save('8x8-gua.png', "PNG")
