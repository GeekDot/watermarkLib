#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from PIL import Image, ImageDraw, ImageFont


# 图像水印
class ImageWatermark(object):

    def __init__(self):
        self.x = None
        self.y = None
        self.text_len = None
        self.image_rgba = None

    # 水印位置
    def watermark_place(self, place):
        # 左上角
        if place == 'top_left':
            return 0, 0
        # 右上角
        elif place == 'top_right':
            return self.x, 0
        # 左下角
        elif place == 'lower_left':
            return 0, self.y
        # 右下角
        elif place == 'lower_right':
            return self.x, self.y
        # 居中
        elif place == 'center':
            return self.x//2, self.y//2
        # 左居中
        elif place == 'left_center':
            return 0, self.y//2
        # 右居中
        elif place == 'right_center':
            return self.x, self.y//2
        # 上居中
        elif place == 'top_center':
            return self.x//2, 0
        # 下居中
        elif place == 'lower_center':
            return self.x//2, self.y
        # 背景覆盖 - place == 'cover'
        else:
            _x = []
            _y = []
            for x in range(0, self.image_rgba.size[0], self.text_len*40+100):
                for y in range(0, self.image_rgba.size[1], 200):
                    _x.append(x)
                    _y.append(y)
            return [_x, _y]

    # 主程序
    def watermark(self, src, **kwargs):

        path, file = os.path.split(src)
        name, suffix = os.path.splitext(file)
        print(name, suffix)

        dest = kwargs.get('dest', '%s/%s' % (os.getcwd(), file))
        text = kwargs.get('text', '图像水印')
        font = kwargs.get('font', 'Medium.ttf')
        size = kwargs.get('size', 36)
        place = kwargs.get('place', 'cover')
        fill = kwargs.get('fill', (0, 0, 0, 50))
        debug = kwargs.get('debug', False)

        # 源图像
        image = Image.open(src)
        # 将图像转换为 RGBA
        self.image_rgba = image.convert('RGBA')
        # 生成像素大小为源图像的新图像
        image_new = Image.new('RGBA', self.image_rgba.size)
        # 绘制新图像
        image_draw = ImageDraw.Draw(image_new)
        # 水印字体
        text_font = ImageFont.truetype(font, size)
        # 水印字体长度
        self.text_len = len(text)
        # 图像大小
        text_size = image_draw.textsize(text, font=text_font)
        # 水印位置
        self.x = self.image_rgba.size[0]-text_size[0]
        self.y = self.image_rgba.size[1]-text_size[1]

        # 获取水印位置
        pixel = self.watermark_place(place)

        # 添加水印
        if isinstance(pixel, list):
            place_cover = list(zip(pixel[0], pixel[1]))
            for data in place_cover:
                image_draw.text((data[0], data[1]), text=text, font=text_font, fill=fill)
            image_new = image_new.rotate(-45)
        else:
            image_draw.text((pixel[0], pixel[1]), text=text, font=text_font, fill=fill)

        image_watermark = Image.alpha_composite(self.image_rgba, image_new)

        # 将 RGBA 转换为 RBG
        image_watermark = image_watermark.convert('RGB')

        # 保存文件
        image_watermark.save(dest)

        # DEBUG
        if debug is True:
            image_watermark.show()

        return dest


iwt = ImageWatermark()
