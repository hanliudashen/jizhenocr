#!/usr/bin/python
# -*- coding: UTF-8 -*-
#极诊团队
#Author 刘翰
import  tableocr
from PIL import Image

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('niao.jpg')

# """ 调用通用文字识别, 图片参数为本地图片 """
# tableocr.client.basicGeneral(image);


# 打开验证码图片
images = Image.open('niao.jpg')
# 加载一下图片防止报错，此处可以省略
images.load()
# 调用show来展示图片，调试用此处可以省略
images.show()
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
ocrji=tableocr.client.basicGeneral(image, options)
print(ocrji)

