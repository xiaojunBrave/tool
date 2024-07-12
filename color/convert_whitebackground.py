"""
@Project :tool
@File    :convert_whitebackground.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/26 13:12
"""
import cv2
def change_background_to_white(image_path, output_path):
    # 读取图片
    image = cv2.imread(image_path)

    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用大津算法进行二值化
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    inverted_binary = cv2.bitwise_not(binary)

    # 保存结果图片
    cv2.imwrite(output_path, inverted_binary)

# 使用示例
change_background_to_white('D:\\Desktop\\1719378485004.jpg', 'D:\\Desktop\\1719378485004_t_8.png')


