"""
@Project :tool
@File    :test_with_depth.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/29 10:39
"""
import data_depth as dt
import numpy as np
import sympy as sp
import tool as tl
from numpy.linalg import inv
import caculate_matrix_withDepthInfo as c
X = c.X
camera_positions = dt.camera_coordinates_t.copy()
tcp_bases = dt.take_photos_coordinates_t.copy()
test_cameras_postions = np.ones((camera_positions.shape[0],3),dtype=float)
for i in range(camera_positions.shape[0]):
    test_cameras_postions[[i], :] = camera_positions[i,0:3]
# print(c_positions)
test_cameras_postions_argument = np.c_[test_cameras_postions, np.ones((test_cameras_postions.shape[0], 1), dtype=float)]
result = test_cameras_postions_argument.dot(X)

for i in range(result.shape[0]):
    # 创建一个对角矩阵
    diagonal_matrix = sp.diag(1, 1, 1)
    r_t_matrix = np.c_[np.r_[diagonal_matrix, np.array([[0, 0, 0]], dtype=float)], np.array([[result[i][0], result[i][1],
                                                                                       result[i][2] , 1.0]],
                                                                                     dtype=float).T]
    tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_bases[i,:])

    # print(np.array(tcp_base_r_t_matrix.dot(r_t_matrix)))\
    r = np.array(tcp_base_r_t_matrix.dot(r_t_matrix))
    print(r[:,3])

