# qrcode_learn
使用python制作二维码

# 模块学习

## qrcode模块
需要安装：`pip install qrcode`
最简单方法：
```python
import qrcode

img = qrcode.make('想要扫码得到的内容')
img.save('保存路径')
```

## 知识点
搞了一个自动产生密码并生成其二维码的代码，还把他搞到了手机上，这里还是有一些新东西

### ASCII码
- 将ASCII码编号转换成字符：`chr(number)`，number必须是0~255的整数
- 将字符转换成ASCII码编号：`ord(character)`，参数必须是单个字符

### 列表转化成字符串
- 之前学过的，没怎么用都忘了
 - 用法：`'用什么连接'.join(目标列表)`
 - 与之相对的是split：`str.split('a', num)` // a表示分隔符，num表示分割多少次

### 安卓手机使用python
- 使用的是`Pydroid`软件，反正锤子应用市场有
- 还是比较好用的，里面含有终端命令行，可以安装模块。
- 因为没用到啥高大上的功能，目前感觉和电脑使用没啥区别，就是打字不太方便。

*——by 秦小炅 2018.10.19*

## 添加logo项目

### qrcode一些方法

```python
qr = qrcode.QRCode( # 实例化为二维码生成设置一些参数
              version=1,  # 设置容错率为最高
              error_correction=qrcode.ERROR_CORRECT_H, # 用于控制二维码的错误纠正程度
              box_size=8, # 控制二维码中每个格子的像素数，默认为10
              border=1, # 二维码四周留白，包含的格子数，默认为4
              #image_factory=None,  保存在模块根目录的image文件夹下
              #mask_pattern=None
              )

qr.add_data(content) # 想要二维码指向的内容
qr.make(fit=True) # 生成二维码（在内部是png图片）

img = qr.make_image() # 生成一个图像对象用于处理
img = img.convert('RGBA') # 设置色彩模式
img.paste(logo, '(坐标)', logo) # logo是要粘贴的图片，这一步就是将二者合成
img.save('路径') # 保存图片
```

### PIL一些方法
这个项目还需要用到PIL库，python3的PIL就是pillow，需要安装：`pip install pillow`

```python
from PIL import Image

logo = Image.open('图片路径')
logo.size # 得到图片尺寸
logo.resize((w, h), Image.ANTIALIAS) # 修改图片尺寸
logo.convert('RGBA') # 设置图片色彩
# 一个重点是在生成二维码的项目中，被粘贴图片一定要设置成RGBA格式，否则会出错
```

## gif二维码
这里要用到`myqr`库，需要安装：`pip install myqr`

```python
from MyQR import myqr

myqr.run(
        words = content, # 二维码要指向的内容，不能含有中文字符，在程序的当前目录中产生相应的二维码图片文件，默认命名为” qrcode.png
        version = 1, # 设置容错率为最高默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H
        level = 'H', # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture = logo, # 用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
        colorized = True, # 可以使产生的图片由黑白(False)变为彩色(True)的
        contrast = 1.0, # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
        brightness = 1.0, # 用来调节图片的亮度，其余用法和取值与 -con 相同
        save_name = name, # 控制文件名，格式可以是 .jpg， .png ，.bmp ，.gif
        # save_dir = path # 保存文件夹
        )
```

*——by 秦小炅 2018.10.20*
