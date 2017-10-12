from PIL import Image, ImageDraw
from numpy import cos, sin, pi

B2G = {
    '000':'000',
    '001':'001',
    '010':'010',
    '011':'011',
    '100':'111',
    '101':'110',
    '110':'101',
    '111':'100'
    }

def int2bin(dec,nd=None):
    if type(nd)==type(None):
        if dec>=1:
            nd=int(log(dec)/log(2))+1
        else:
            nd=1
    return (('{0:0'+str(nd)+'b}').format(int(dec)))[-nd:]


def draw_yang(im, length=10,width=2,fill=0, center=(0,0), angle=0):
    draw = ImageDraw.Draw(im)
    halfLength = 0.5*length
    arcDeg = angle * pi / 180.0
    x0 = round(center[0] - halfLength * sin(arcDeg))
    x1 = round(center[0] + halfLength * sin(arcDeg))
    y0 = round(center[1] + halfLength * cos(arcDeg))
    y1 = round(center[1] - halfLength * cos(arcDeg))
    draw.line((x0,y0,x1,y1),fill=fill,width=width)

def draw_yin(im, length=15, width=2,fill=0, center=(0,0), angle=0):
    draw = ImageDraw.Draw(im)
    arcDeg = angle * pi / 180.0
    x0 = round(center[0] - length/2.0 * sin(arcDeg))
    x1 = round(center[0] - length/6.0 * sin(arcDeg))
    y0 = round(center[1] + length/2.0 * cos(arcDeg))
    y1 = round(center[1] + length/6.0 * cos(arcDeg))
    x2 = round(center[0] + length/2.0 * sin(arcDeg))
    x3 = round(center[0] + length/6.0 * sin(arcDeg))
    y2 = round(center[1] - length/2.0 * cos(arcDeg))
    y3 = round(center[1] - length/6.0 * cos(arcDeg))
    draw.line((x0,y0,x1,y1),fill=fill,width=width)
    draw.line((x2,y2,x3,y3),fill=fill,width=width) 

def draw_gua(im,binary, length=10, width=2, gap=5, fill=0, center=(0,0), angle=0):
    arcDeg = angle * pi / 180.0
    L = len(binary)
    height = (L-1)*gap
    x, y = (center[0]-0.5*height*cos(arcDeg), center[1]-0.5*height*sin(arcDeg))
    for i in range(L):
        s = binary[i]
        if s == '0':
            draw_yin(im, length=length, width=width,fill=fill, center=(x,y), angle=angle)
        else:
            draw_yang(im, length=length, width=width,fill=fill, center=(x,y), angle=angle)
        x = x + gap * cos(arcDeg)
        y = y + gap * sin(arcDeg)
