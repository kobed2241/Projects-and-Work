from Myro import *

obamaDarkBlue = makeColor(0,51,76)
obamaRed = makeColor(217,26,33)
obamaBlue = makeColor(112,150,158)
obamaYellow = makeColor(252,227,166)

pic = makePicture(pickAFile())
pixels = getPixels(pic)

for pixel in pixels:
    gray = getGray(pixel)
    if gray > 180:
        setColor(pixel, obamaYellow)
    elif gray > 120:
        setColor(pixel, obamaBlue)
    elif gray > 60:
        setColor(pixel, obamaRed)
    else:
        setColor(pixel, obamaDarkBlue)
    
    

show(pic)
