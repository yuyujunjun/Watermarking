# -*- coding:utf-8 -*-
import sys
secret = sys.argv[1]
dest=sys.argv[2]
from PIL import Image
import numpy
#preim1=Image.open('./secret.png')
#Dest=Image.open('./dest.jpg')
preim1=Image.open(secret)
Dest=Image.open(dest)
Dest.show()
size=(0,0)
#we should change the size of secret img so that we can store it in dest img
if(Dest.width>Dest.height):
    size=(int(Dest.height),int(Dest.height))
else:
    size=(int(Dest.width),int(Dest.width))
#change mode of secret img
im1=preim1.convert('P')
im1=im1.resize(size)
Dest=Dest.convert('RGBA')
r,g,b,a=Dest.split()

temp=im1
def to8bits(a):
    str2bits=bin(a)
    return str2bits[2:].zfill(8)
def split4parts(a):
    bits=to8bits(a)
    if(len(bits)!=8):
        print('wrong')
    x=[0,0,0,0]
    x[0]=bits[0:2]
    x[1]=bits[2:4]
    x[2]=bits[4:6]
    x[3]=bits[6:8]
    return x
def merge4parts(x):
	result=x[0]+x[1]+x[2]+x[3]
	result=int(result,2)
	return result

def addparts(pos,px):
    pix=r.getpixel(pos)
    pix=to8bits(pix)
    pix=pix[0:len(pix)-2]+px[0]
    pix=int(pix,2)
    r.putpixel(pos,pix)
    pix=g.getpixel(pos)
    pix=to8bits(pix)
    pix=pix[0:len(pix)-2]+px[1]
    pix=int(pix,2)
    g.putpixel(pos,pix)
    pix=b.getpixel(pos)
    pix=to8bits(pix)
    pix=pix[0:len(pix)-2]+px[2]
    pix=int(pix,2)
    b.putpixel(pos,pix)
    pix=a.getpixel(pos)
    pix=to8bits(pix)
    pix=pix[0:len(pix)-2]+px[3]
    pix=int(pix,2)
    a.putpixel(pos,pix)
def right2parts(pos):
    px=[0,0,0,0]
    pix=r.getpixel(pos)
    pix=to8bits(pix)
    px[0]=pix[len(pix)-2:len(pix)]
    pix=g.getpixel(pos)
    pix=to8bits(pix)
    px[1]=pix[len(pix)-2:len(pix)]
    pix=b.getpixel(pos)
    pix=to8bits(pix)
    px[2]=pix[len(pix)-2:len(pix)]
    pix=a.getpixel(pos)
    pix=to8bits(pix)
    px[3]=pix[len(pix)-2:len(pix)]
    px=merge4parts(px)
    return px
pos=(0,0)
for i in range(size[0]):
    for j in range(size[0]):
        pos=(i,j)
        px=split4parts(im1.getpixel(pos))
        addparts(pos,px)

dest=Image.merge('RGBA',(r,g,b,a))

dest.save('./dest2.png')


        








        



        


