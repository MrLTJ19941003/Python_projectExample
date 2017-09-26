from PIL import Image

im=Image.open('thubnail.jpg')
w,h=im.size
print('image is %s , %s '% (w,h))
im.thumbnail((w*8,h*8))
print('update image is %s , %s ' , (w*8,h*8))
im.save('thumbnail.jpg','jpeg')