from PIL import Image, ImageFilter

#打开一个jpg图像文件：
im = Image.open('test.jpg')
#应用模糊滤镜：
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')