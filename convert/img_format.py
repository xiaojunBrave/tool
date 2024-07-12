"""
@Project :tool
@File    :img_format.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/21 15:00
"""
from PIL import Image
import os

# 输入文件路径
input_path = 'D:\\Desktop\\078c6052-4597-487d-9ccc-3bf4c17fc4de.jfif'
# 输出文件路径
output_path = 'D:\\Desktop\\078c6052-4597-487d-9ccc-3bf4c17fc4de.jpg'

# 打开JFIF图像
with Image.open(input_path) as img:
    # 将图像保存为JPEG格式
    img.save(output_path, 'JPEG')

print(f'Image converted and saved to {output_path}')
