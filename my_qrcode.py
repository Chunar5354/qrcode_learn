# 使用myqr库，可以制作gif二维码

from MyQR import myqr
import os

print('说明：\n1.内容可以是一个文本或者是网址，但不要包含中文字符\n2.logo图片可以是jpg，png，gif，bmp\n3.保存时的图片要与logo图片对应（比如logo图片是gif保存的图片必须也是gif，logo是jpg则需要保存成png格式）')

content = input('请输入二维码指向的内容(不要输入汉字)：')
logo = input('请输入logo图片路径：')
name = input('请输入生成的二维码图片保存名称：')
# path = input('请输入图片保存文件夹路径（保存在相同文件夹可以输入None）：')

myqr.run(
        words = content,
        version = 1,
        level = 'H',
        picture = logo,
        colorized = True,
        contrast = 1.0,
        brightness = 1.0,
        save_name = name,
        # save_dir = path
        )
