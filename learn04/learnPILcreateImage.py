from PIL import Image,ImageFont,ImageFilter,ImageDraw
import random,os
import time
def randint_code():
    code_list=[]     #定义空列表
    for i in range(10):
        code_list.append(str(i))   #添加0-9的数字
    for i  in range(65,91):
        code_list.append(chr(i))   #添加A-Z的字母
    for i in range(97,123):
        code_list.append(chr(i))   #添加a-z的字母
    random_code=random.sample(code_list,1)   #从列表code_list中随机筛选六个
    random_math=''.join(random_code)        #转化为一个字符串
    return random_math             #返回一个字符串
def random_coclor1():  #随机颜色返回三个RGB的值
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def random_coclor2():  #随机颜色返回三个RGB的值
    return (random.randint(32,127),random.randint(0,255),random.randint(0,255))
width=60*4
heigth=60
image=Image.new('RGB',(width,heigth),(255,255,255))  #创建画布

font=ImageFont.truetype('Arial.ttf',36)  #选择字体

draw=ImageDraw.Draw(image)      #创建一个可对image进行操作的对象
for  a in  range(width):
    for b in range(heigth):
        draw.point((a,b),random_coclor1())  #遍历每个像素进行颜色填充
code_list=[]
for  c in  range(6):
    code_math = randint_code()
    code_list.append(code_math)
    draw.text((40*c+10,10),code_math,font=font,fill=random_coclor2()) #text包含三个参数  间距，文本，字体，字体颜色
code_list=''.join(code_list)
print(code_list)
image=image.filter(ImageFilter.DETAIL)
image.show()