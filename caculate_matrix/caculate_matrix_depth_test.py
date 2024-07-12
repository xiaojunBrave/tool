"""
@Project :tool
@File    :caculate_matrix_depth_test.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/7/2 18:33
"""
import data_depth as dt
import numpy as np
import sympy as sp
import tool as tl
from numpy.linalg import inv
import caculate_matrix_withDepthInfo as ca
X = ca.X

tcp_base = dt.take_photos_coordinates_4
camera_coordinates = dt.camera_coordinate_4

tcp_base_r_t_matrixs = []
tcp_base_r_t_matrix_invs = []
for i in range(tcp_base.shape[0]):
    tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_base[i,:])
    tcp_base_r_t_matrixs.append(tcp_base_r_t_matrix)
    tcp_base_r_t_matrix_invs.append(inv(tcp_base_r_t_matrix))

test_cameras_postions = np.ones((camera_coordinates.shape[0],3),dtype=float)
for i in range(camera_coordinates.shape[0]):
    test_cameras_postions[[i], :] = camera_coordinates[i,0:3]
# print(c_positions)
test_cameras_postions_argument = np.c_[test_cameras_postions, np.ones((test_cameras_postions.shape[0], 1), dtype=float)]
result = test_cameras_postions_argument.dot(X)
print(result)
for i in range(result.shape[0]):
    # 创建一个对角矩阵
    diagonal_matrix = sp.diag(1, 1, 1)
    r_t_matrix = np.c_[np.r_[diagonal_matrix, np.array([[0, 0, 0]], dtype=float)], np.array([[result[i][0], result[i][1],
                                                                                              result[i][2] -200, 1.0]],
                                                                                            dtype=float).T]
    # print(np.array(tcp_base_r_t_matrix.dot(r_t_matrix)))\
    tcp_base_r_t_matrix = tcp_base_r_t_matrixs[i]
    print(tcp_base_r_t_matrix)
    r = np.array(tcp_base_r_t_matrix.dot(r_t_matrix))
    # print(r[:,3])