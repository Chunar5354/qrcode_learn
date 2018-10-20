# 一个获得随机密码并生成其二维码的程序

import qrcode
import random


len_key = random.randint(11,16)
index_key = 0
key_list = []

while index_key <= len_key:
    key_num = random.randint(33,122) # ASCII码的字符和数字、字母范围
    key_word = chr(key_num) # ASCII码的转换
    key_list.append(key_word)
    index_key += 1

keyword = ''.join(key_list) # 列表转字符串

name = input('请输入要被设置密码的内容：')
img = qrcode.make(keyword)
img.save('{}.jpg'.format(name))

print('The keyword is: ', keyword)
print('二维码生成')
