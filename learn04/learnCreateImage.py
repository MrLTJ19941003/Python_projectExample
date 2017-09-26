from PIL import Image,ImageFilter,ImageDraw,ImageFont

import random

#随机字母
def rndchr():
    return chr(random.randint(65,90))

def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndcolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))

font=ImageFont.truetype('Arial.ttf',36)
drow=ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        drow.point((x,y),fill=rndcolor())

for t in range(4):
    drow.text((60*t+10,10),rndchr(),font=font,fill=rndcolor2())
image=image.filter(ImageFilter.DETAIL)
#image.save('code.jpg','jpeg')
image.show()