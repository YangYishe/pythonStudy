"""
pillow操作图像
"""

from PIL import Image,ImageFilter

def main():
    image=Image.open('065_S.jpg')
    print(image.mode)
    # 1.图像剪切
    # rect=80,20,310,360
    # image.crop(rect).show()
    # 2.生成缩略图
    # size=128,128
    # image.thumbnail(size)
    # image.show()
    # 3.缩放和黏贴图像
    # image2=Image.open('cat2.jpg')
    # rect = 80, 20, 310, 360
    # guido_head=image2.crop(rect)
    # width,height=guido_head.size
    # image.paste(guido_head.resize((int(width/1.5),int(height/1.5))),(172,40))
    # image.show()
    # 4.旋转和翻转
    # image.rotate(180).show()
    # image.transpose(Image.FLIP_LEFT_RIGHT).show()
    # 5.操作像素
    # for x in range(80,310):
    #     for y in range(20,360):
    #         image.putpixel((x,y),(128,128,128))
    # image.show()
    # 6.滤镜效果
    # image.filter(ImageFilter.CONTOUR).show()

    pass

if __name__ == '__main__':
    main()