"""
@Project :tool
@File    :getHSV.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/10/23 14:08
"""
import cv2
# 鼠标事件回调函数
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y][x]
        print('Pixel ({}, {}): RGB({}, {}, {})'.format(x, y, r, g, b))

        h, s, v = img_hsv[y][x]
        print('Pixel ({}, {}): HSV({}, {}, {})'.format(x, y, h, s, v))
        print()

# 读取图像
img = cv2.imread(r'D:\Desktop\\flower\\fake_flowers\\1698043024.png')

# 转换为HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 创建窗口并绑定鼠标事件
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse)

while True:
    # 在窗口中显示图像
    cv2.imshow('image', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 关闭窗口
cv2.destroyAllWindows()



