#Sean Donaldson 10/22/2020
from jes import *

def collage():

    file = 'falls.jpg'
    picture = makePicture(file)

    sig = 'signature.jpg'
    signature = makePicture(sig)
    small_sig = scaleDown(signature, 15)


    smaller_pic = scaleDown(picture, 12)
    picWidth = getWidth(smaller_pic)
    picHeight = getHeight(smaller_pic)

    canvas = makeEmptyPicture(picWidth * 5, picHeight * 3)








    copy(smaller_pic, canvas, picWidth, picHeight)
    copy(smaller_pic, canvas, 0, 0)
    copy(smaller_pic, canvas, picWidth, 0)
    copy(smaller_pic, canvas, 0, picHeight)
    copy(smaller_pic, canvas, 0, picHeight * 2)
    copy(smaller_pic, canvas, picWidth * 2, picHeight * 2)
    copy(smaller_pic, canvas, picWidth * 2, 0)
    copy(smaller_pic, canvas, picWidth, picHeight * 2)
    copy(smaller_pic, canvas, picWidth * 2, picHeight)
    copy(smaller_pic, canvas, picWidth * 3, 0)
    copy(smaller_pic, canvas, picWidth * 3, picHeight)
    copy(smaller_pic, canvas, picWidth * 3, picHeight * 2)
    copy(smaller_pic, canvas, picWidth * 4, 0)
    copy(smaller_pic, canvas, picWidth * 4, picHeight)
    copy(smaller_pic, canvas, picWidth * 4, picHeight * 2)

    chromaSig(small_sig, canvas, 925, 525)

    red(canvas)
    green(canvas)
    blue(canvas)
    lighten(canvas)
    darken(canvas)
    edge(canvas)
    edgedetect(canvas)
    gray_scale(canvas)
    show(canvas)


    writePictureTo(canvas,'Sean_Donaldson_Collage.jpg')

def gray_scale(pic):
    for x in range(((getWidth(pic) // 5) * 2), ((getWidth(pic) // 5) * 3)):
        for y in range(0, ((getHeight(pic) // 3 )  ) ):
            p = getPixel(pic, x, y)
            intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
            setColor(p,makeColor(intensity,intensity,intensity))

    for x in range(((getWidth(pic) // 5) * 2), ((getWidth(pic) // 5) * 3)):
        for y in range(((getHeight(pic) // 3 ) *2 ), ((getHeight(pic) // 3 ) *3 ) ):
            p = getPixel(pic, x, y)
            intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
            setColor(p,makeColor(intensity,intensity,intensity))



def chromaSig(source, target, targetX, targetY):
    for x in range(0, getWidth(source)):
        for y in range(0, getHeight(source)):
            px = getPixel(source, x, y)
            color = getColor(px)
            targ = getPixel(target, x + targetX, y + targetY)
            if distance (black, color) < 100:
                setColor(targ, white)


def scale(src,canvas,factor):
    sourceX = 0
    for targetX in range(0, int(getWidth(src) * factor)):
        sourceY = 0
        for targetY in range(0, int(getHeight(src) * factor)):
            color = getColor(getPixel(src, int(sourceX), int(sourceY)))
            setColor(getPixel(canvas, targetX, targetY), color)
            sourceY = sourceY + 1.0 / factor
        sourceX = sourceX + 1.0 / factor



def scaleDown(pic, factor):
    canvas = makeEmptyPicture(int(getWidth(pic) / factor), int(getHeight(pic) / factor))
    scale(pic, canvas, 1.0 / factor)
    return canvas


def copy(source, target, targX, targY):
    targetX = targX
    for sourceX in range(0, getWidth(source)):
        targetY = targY
        for sourceY in range(0, getHeight(source)):
            px = getPixel(source, sourceX, sourceY)
            tx = getPixel(target, targetX, targetY)
            setColor(tx, getColor(px))
            targetY = targetY + 1
        targetX = targetX + 1



def lighten(pic):
    for x in range(((getWidth(pic) // 15) * 2 ),       ((getWidth(pic) // 15) * 3)     ):
        for y in range(    (getHeight(pic)  // 9)  ,            ((getHeight(pic)  // 9) * 3  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15)  ),       ((getWidth(pic) // 15) * 2)     ):
        for y in range(    ((getHeight(pic)  // 9) * 2) ,            ((getHeight(pic)  // 9) * 3  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            setColor(px,color)



    for x in range(((getWidth(pic) // 15) * 2),       ((getWidth(pic) // 15) * 3)     ):
        for y in range(    0 ,            ((getHeight(pic)  // 9)    )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)


    for x in range(((getWidth(pic) // 15) ),       ((getWidth(pic) // 15) * 2)     ):
        for y in range(    ((getHeight(pic)  // 9)    ) ,            ((getHeight(pic)  // 9)   *2 )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(0,       ((getWidth(pic) // 15))     ):
        for y in range(    ((getHeight(pic)  // 9) *2   ) ,            ((getHeight(pic)  // 9)   *3 )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)




    for x in range(0 ,       ((getWidth(pic) // 15) * 2)     ):
        for y in range(    0 ,            ((getHeight(pic)  // 9)    )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(0 ,       ((getWidth(pic) // 15) )     ):
        for y in range(   ((getHeight(pic)  // 9)    )  ,            ((getHeight(pic)  // 9)  * 2  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)





    for x in range(0 ,       ((getWidth(pic) // 15) )     ):
        for y in range(   ((getHeight(pic)  // 9)   *3 )  ,            ((getHeight(pic)  // 9)  * 6  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) ) ,       ((getWidth(pic) // 15) * 2)     ):
        for y in range(   ((getHeight(pic)  // 9)   *3 )  ,            ((getHeight(pic)  // 9)  * 6  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)




    for x in range(((getWidth(pic) // 15) * 2 ) ,       ((getWidth(pic) // 15) * 3)     ):
        for y in range(   ((getHeight(pic)  // 9)   *3 )  ,            ((getHeight(pic)  // 9)  * 6  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            setColor(px,color)








    for x in range(((getWidth(pic) // 15)  ) ,       ((getWidth(pic) // 15) * 3)     ):
        for y in range(   ((getHeight(pic)  // 9)   *6 )  ,            ((getHeight(pic)  // 9)  * 7  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) * 2 ) ,       ((getWidth(pic) // 15) * 3)     ):
        for y in range(   ((getHeight(pic)  // 9)   *7 )  ,            ((getHeight(pic)  // 9)  * 8  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(0 ,       ((getWidth(pic) // 15))     ):
        for y in range(   ((getHeight(pic)  // 9)   *6 )  ,            ((getHeight(pic)  // 9)  * 7  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15)) ,       ((getWidth(pic) // 15)*2)     ):
        for y in range(   ((getHeight(pic)  // 9)  *7  )  ,            ((getHeight(pic)  // 9)  * 8  )      ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15)*2) ,       ((getWidth(pic) // 15)*3)     ):
        for y in range(   ((getHeight(pic)  // 9)  *8  )  ,            getHeight(pic)        ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range(0 ,       (getWidth(pic) // 15)     ):
        for y in range(   ((getHeight(pic)  // 9)  *7  )  ,            getHeight(pic)        ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)

    for x in range((getWidth(pic) // 15) ,       ((getWidth(pic) // 15) *2 )   ):
        for y in range(   ((getHeight(pic)  // 9)  *8 )  ,            getHeight(pic)        ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeLighter(color)
            color = makeLighter(color)
            color = makeLighter(color)
            setColor(px,color)













def darken(pic):
    #first box darken
    for x in range(((getWidth(pic) // 15) * 12 ),       ((getWidth(pic) // 15)  * 14)     ):
        for y in range(((getHeight(pic) // 9) * 2),        ((getHeight(pic) // 9) * 3)             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) * 12 ),       ((getWidth(pic) // 15)  * 13)     ):
        for y in range(((getHeight(pic) // 9) ),        ((getHeight(pic) // 9) * 2)             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            setColor(px,color)





    for x in range(((getWidth(pic) // 15) * 12 ),       ((getWidth(pic) // 15)  * 13)     ):
        for y in range(0,        ((getHeight(pic) // 9) )             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) * 13 ),       ((getWidth(pic) // 15)  * 14)     ):
        for y in range(((getHeight(pic) // 9) ),        ((getHeight(pic) // 9) * 2)             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) * 14 ),       getWidth(pic)     ):
        for y in range(((getHeight(pic) // 9)*2 ),        ((getHeight(pic) // 9) * 3)             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)




    for x in range(((getWidth(pic) // 15) * 13 ),       getWidth(pic)     ):
        for y in range(0        ,getHeight(pic) // 9             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)

    for x in range(((getWidth(pic) // 15) * 14 ),       getWidth(pic)     ):
        for y in range(((getHeight(pic) // 9) ),        ((getHeight(pic) // 9) * 2)             ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)








#second box darken
    for x in range(((getWidth(pic) // 15) * 14 ),        getWidth(pic)    ):
        for y in range(((getHeight(pic) // 9) * 3),        ((getHeight(pic) // 9) * 6)):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)

    for x in range((((getWidth(pic) // 15) * 13 )),       ((getWidth(pic) // 15) * 14 )     ):
        for y in range(((getHeight(pic) // 9) * 3),        ((getHeight(pic) // 9) * 6)):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)

    for x in range((((getWidth(pic) // 15) * 12 )),       ((getWidth(pic) // 15) * 13 )     ):
        for y in range(((getHeight(pic) // 9) * 3),        ((getHeight(pic) // 9) * 6)):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            setColor(px,color)






#third box darken
    for x in range(((getWidth(pic) // 15) * 12 ),    ((getWidth(pic) // 15)  * 14)     ):
        for y in range(((getHeight(pic) // 9) * 6),        ((getHeight(pic) // 9) * 7)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            setColor(px,color)


    for x in range(((getWidth(pic) // 15) * 12 ),    ((getWidth(pic) // 15)  * 13)     ):
        for y in range(((getHeight(pic) // 9) * 7),        ((getHeight(pic) // 9) * 8)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            setColor(px,color)


    for x in range(((getWidth(pic) // 15) * 14 ),    getWidth(pic)     ):
        for y in range(((getHeight(pic) // 9) * 6),        ((getHeight(pic) // 9) * 7)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)


    for x in range(((getWidth(pic) // 15) * 13 ),    ((getWidth(pic) // 15) * 14)     ):
        for y in range(((getHeight(pic) // 9) * 7),        ((getHeight(pic) // 9) * 8)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)





    for x in range(((getWidth(pic) // 15) * 12 ),    ((getWidth(pic) // 15)  * 13)     ):
        for y in range(((getHeight(pic) // 9) * 8),        ((getHeight(pic) // 9) * 9)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)






    for x in range(((getWidth(pic) // 15) * 13 ),    getWidth(pic)     ):
        for y in range(((getHeight(pic) // 9) * 8),        getHeight(pic)           ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)


    for x in range(((getWidth(pic) // 15) * 14 ),    getWidth(pic)     ):
        for y in range(((getHeight(pic) // 9) * 7),        ((getHeight(pic) // 9) * 8)            ):
            px = getPixel(pic,x,y)
            color = getColor(px)
            color = makeDarker(color)
            color = makeDarker(color)
            color = makeDarker(color)
            setColor(px,color)


def edge(pic):
    for x in range(((getWidth(pic) // 5) * 3),       ((getWidth(pic) // 5) * 4)     ):
        for y in range(0,getHeight(pic) ):
            px = getPixel(pic,x,y)
            x = getX(px)
            y = getY(px)
            if y < getHeight(pic)-1 and x < getWidth(pic)-1:
                sum1 = getRed(px)+getGreen(px)+getBlue(px)
                botrt = getPixel(pic,x+1,y+1)
                sum2 = getRed(botrt) + getGreen(botrt) + getBlue(botrt)
                diff = abs(sum2-sum1)
                newcolor = makeColor(diff,diff,diff)
                setColor(px,newcolor)

def luminance(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)

    return (r+g+b)/3

def edgedetect(pic):
    for x in range(((getWidth(pic) // 5) ),       ((getWidth(pic) // 5) * 2)     ):
        for y in range(0,   getHeight(pic)) :
            px = getPixel(pic,x,y)
            x = getX(px)
            y = getY(px)
            if y < getHeight(pic)-1 and x < getWidth(pic)-1:
                botrt = getPixel(pic,x+1,y+1)
                thislum = luminance(px)
                brlum = luminance(botrt)
                if abs(brlum-thislum) > 10:
                    setColor(px,black)
                if abs(brlum-thislum) <= 10:
                    setColor(px,white)

def red(pic):
    for x in range(0,   ((getWidth(pic) // 5 )     *2   )):
        for y in range(0, ((getHeight(pic) // 3)   ) ):
            p = getPixel(pic,x,y)
            value=getBlue(p)
            setBlue(p,value*0.6)
            value=getGreen(p)
            setGreen(p,value*0.6)

    for x in range(((getWidth(pic) // 5 )     *3   ),   (getWidth(pic))):
        for y in range(0, ((getHeight(pic) // 3)   ) ):
            p = getPixel(pic,x,y)
            value=getBlue(p)
            setBlue(p,value*0.6)
            value=getGreen(p)
            setGreen(p,value*0.6)
def green(pic):
    for x in range(  0      ,     ((getWidth(pic)  // 5)  *2)    ):
        for y in range(((getHeight(pic) // 3)   ), ((getHeight(pic) // 3) *2  )):
            p = getPixel(pic,x,y)
            value=getRed(p)
            setRed(p,value*0.6)
            value=getBlue(p)
            setBlue(p,value*0.6)


    for x in range(((getWidth(pic)  // 5)  *3), getWidth(pic)):
        for y in range(((getHeight(pic) // 3)   ), ((getHeight(pic) // 3) *2  )):
            p = getPixel(pic,x,y)
            value=getRed(p)
            setRed(p,value*0.6)
            value=getBlue(p)
            setBlue(p,value*0.6)
def blue(pic):
    for x in range(  0      ,     ((getWidth(pic)  // 5)  *2)    ):
        for y in range(((getHeight(pic) // 3) *2  ), (getHeight(pic) )):
            p = getPixel(pic,x,y)
            value=getRed(p)
            setRed(p,value*0.6)
            value=getGreen(p)
            setGreen(p,value*0.6)


    for x in range(((getWidth(pic)  // 5)  *3), getWidth(pic)):
        for y in range(((getHeight(pic) // 3) *2  ), (getHeight(pic) )):
            p = getPixel(pic,x,y)
            value=getRed(p)
            setRed(p,value*0.6)
            value=getGreen(p)
            setGreen(p,value*0.6)
collage()