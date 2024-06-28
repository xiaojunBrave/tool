"""
@Project :tool
@File    :data_depth.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/28 18:58
"""
import numpy as np
move_brush = np.array([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,200],
                         [0,0,0,1]])
# data
data_version = 1
tcp_base_1 = np.array([0.01414,-0.28070,0.24574,0.066, -1.445, 2.814])
camera_coordinate_1 = np.array([
                     [-0.0039, 0.0268, 0.4560, 0.066, -1.445, 2.814],
                     [0.1013, 0.0610, 0.5060, 0.066, -1.445, 2.814],
                     [-0.0140, -0.0153, 0.2910, 0.066, -1.445, 2.814],
                     [0.0608, -0.0774, 0.2910, 0.066, -1.445, 2.814],
                     [0.0920, 0.0179, 0.3430, 0.066, -1.445, 2.814],
                     [0.0323, 0.0163, 0.3260, 0.066, -1.445, 2.814],
])
tcp_coordinate_1 = np.array([
    [48.05, -546.80, 401.65, 0.066, -1.445, 2.814],
    [-57.17, -604.02, 386.33, 0.066, -1.445, 2.814],
    [58.62, -388.59, 400.05, 0.066, -1.445, 2.814],
    [-13.67, -364.49, 459.73, 0.066, -1.445, 2.814],
    [-47.70, -440.54, 383.44, 0.066, -1.445, 2.814],
    [9.76, -423.38, 379.61, 0.066, -1.445, 2.814]
])
# ****************data_version_4*************************
tcp_bases = [tcp_base_1]
camera_coordinates = [camera_coordinate_1]
tcp_coordinates = [tcp_coordinate_1]

index = data_version - 1
camera_coordinate = camera_coordinates[index]
tcp_coordinate = tcp_coordinates[index]
tcp_base = tcp_bases[index]
