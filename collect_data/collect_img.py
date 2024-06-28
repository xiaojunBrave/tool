"""
@Project :tool
@File    :collect_img.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/10/27 14:25
"""
import cv2
import time
from PyCameraList.camera_device import test_list_cameras, list_video_devices, list_audio_devices
save_dir = '../../datasets/fake_flower_v1/images/train/'
width = 640
height = 480
fps = 30

def save_frame(frame,num):
    # 生成唯一的文件名
    filename = save_dir + str(time.time())+".jpg"
    # 保存图像
    cv2.imwrite(filename, frame)

def main(resolution=(640, 480), fps=30):
    # 打开摄像头 选择正确摄像头id
    cap = cv2.VideoCapture(3)
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    original_resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(f"原始摄像头帧率: {original_fps}")
    print(f"原始摄像头分辨率: {original_resolution}")
    # 设置分辨率和帧率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    cap.set(cv2.CAP_PROP_FPS, fps)
    num = 0
    while True:
        # 读取摄像头图像
        ret, frame = cap.read()
        if ret:
            # 显示图像
            cv2.imshow('Camera', frame)
            # 每0.3秒保存一张图像
            if cv2.waitKey(300):
                save_frame(frame,num)
                num +=1
        # 按下 'q' 键退出循环
        if cv2.waitKey(1) == ord('q'):
            break
    # 释放摄像头资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # 设置分辨率为640x480，帧率为30
    # cameras = list_video_devices()
    # print(dict(cameras))
    main(resolution=(width, height), fps=fps)