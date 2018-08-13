import requests
from io import BytesIO
from PIL import Image,ImageFilter,ImageEnhance
from pytesseract import image_to_string
import douban.baidu

# 验证码识别
def get_captcha(data):
    image = Image.open(BytesIO(data))
    #image.show()

    image_enh = ImageEnhance.Brightness(image)
    image_enh_bright = image_enh.enhance(2.0)
    #image_enh_bright.show()

    image_enh = ImageEnhance.Color(image_enh_bright)
    image_enh_color = image_enh.enhance(1.5)
    #image_enh_color.show()

    image_enh = ImageEnhance.Sharpness(image_enh_color)
    image_enh_sharp = image_enh.enhance(2)
    #image_enh_sharp.show()

    image_l = image_enh_sharp.convert('L')
    #image_l.show()

    image_point = image_l.convert('1')
    #image_point.show()
    # ========================='
    #captcha = image_to_string(image_point ,lang='eng', config='-psm 8')
    # with open('checkcode.jpg', 'wb') as f:
    #     f.write(captcharesponse.content)
    #     f.close()
    # os.startfile('checkcode.jpg')
    # textss = douban.baidu.getImageString1('checkcode.jpg')
    # print(textss)
    image_point.save('plcode.jpg')
    textss = douban.baidu.getImageString1('plcode.jpg')
    textss = textss.strip()
    print(textss.strip())
    #print(captcha.strip())
    image.close()

    return textss#captcha


# result = requests.get('https://www.douban.com/misc/captcha?id=at6c5zYtk1bp8K5wjRjjv3ww:en&size=s')
# get_captcha(result.content)