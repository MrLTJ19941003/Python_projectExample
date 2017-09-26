from PIL import Image,ImageFilter


def fuzzy(path):
    im=Image.open(path)
    im2=im.filter(ImageFilter.BLUR)
    im2.save('test1.jpg','jpeg')

fuzzy('IMG_4303.JPG')