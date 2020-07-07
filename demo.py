#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from watermarkLib import iwt

"""
'top_left': '左上角',
'top_right': '右上角',
'lower_left': '左下角',
'lower_right': '右下角',
'center': '居中',
'left_center': '左居中',
'right_center': '右居中',
'top_center': '上居中',
'lower_center': '下居中',
'cover': '背景覆盖',
"""

# 源图像
src = '/Users/zhangyi/Downloads/WechatIMG222.jpeg'
data = iwt.watermark(src)
print(data)

# 目标图像
dest = './baidu.png'
# 水印文字
text = '绝密'
# data = iwt.watermark(src, dest=dest, text=text)
# print(data)

# 水印字体
font = './Medium.ttf'
# 水印字号
size = 36
# 水印位置
place = 'cover'
# 水印 RGB 颜色、透明度
fill = (0, 0, 0, 50)

# data = iwt.watermark(src, dest=dest, text=text, font=font, size=size, place=place, fill=fill, debug=True)

