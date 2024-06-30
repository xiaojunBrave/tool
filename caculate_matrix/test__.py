"""
@Project :tool
@File    :test__.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/29 12:23
"""
import numpy as np
import cv2
from scipy.spatial.transform import Rotation as R
import data_depth as dt
# TCP位姿 (四个位姿数据, 每个数据是6维向量, 包含位置和旋转矢量)
selected_row = [0, 2, 3, 4]
# 输入数据：4个TCP的六维位姿和目标物体的四个三维位置
tcp_poses = dt.tcp_base[selected_row,:]

# 目标物体在相机坐标系中的三维位置
object_positions_camera = dt.camera_coordinate[selected_row,:]


# 目标物体在机械臂基座坐标系中的三维位置
object_positions_base = dt.tcp_coordinate[selected_row,0:3]

# 将TCP位姿转换为旋转矩阵和平移向量
def pose_to_rt(pose):
    position = pose[:3]
    rotation_vector = pose[3:]
    rotation_matrix = R.from_rotvec(rotation_vector).as_matrix()
    return rotation_matrix, position

# 计算手眼标定的转换矩阵
def hand_eye_calibration(tcp_poses, object_positions_camera, object_positions_base):
    R_gripper2base = []
    t_gripper2base = []
    R_target2cam = []
    t_target2cam = []

    for pose in tcp_poses:
        R, t = pose_to_rt(pose)
        R_gripper2base.append(R)
        t_gripper2base.append(t)

    for cam_pos, base_pos in zip(object_positions_camera, object_positions_base):
        R_target2cam.append(np.eye(3))  # 假设没有旋转，只考虑平移
        t_target2cam.append(np.array(cam_pos) - np.array(base_pos))

    R_gripper2base = np.array(R_gripper2base)
    t_gripper2base = np.array(t_gripper2base)
    R_target2cam = np.array(R_target2cam)
    t_target2cam = np.array(t_target2cam)

    R_cam2gripper, t_cam2gripper = cv2.calibrateHandEye(
        R_gripper2base, t_gripper2base,
        R_target2cam, t_target2cam
    )

    return R_cam2gripper, t_cam2gripper

R_cam2gripper, t_cam2gripper = hand_eye_calibration(tcp_poses, object_positions_camera, object_positions_base)

print("相机坐标系到TCP末端坐标系的旋转矩阵:")
print(R_cam2gripper)
print("相机坐标系到TCP末端坐标系的平移向量:")
print(t_cam2gripper)
