# 使用qrcode库制作含有自己logo的二维码

import qrcode
from PIL import Image

def make_a_qrcode(content, which_picture, name):
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.ERROR_CORRECT_H, border = 2)

    qr.add_data(content)
    qr.make(fit = True)

    img = qr.make_image()
    img = img.convert("RGB")
    logo = Image.open('{}'.format(which_picture))

    w, h = img.size
    logo_w = int(w/4)
    logo_h = int(h/4)

    rel_w = int((w-logo_w)/2)
    rel_h = int((h-logo_h)/2)
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
    logo = logo.convert("RGBA") # 这里logo必须变成RGBA格式，否则会出错
    img.paste(logo, (rel_w, rel_h), logo)

    img.save('{}'.format(name))

content = input('想要二维码指向的内容：')
which_picture = input('设置logo图片（输入路径）：')
name = input('图片保存路径：')

make_a_qrcode(content, which_picture, name)
