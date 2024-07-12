"""
@Project :tool
@File    :caculate_matrix_withDepthInfo.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/28 18:56
"""
import data_depth as dt
import numpy as np
import sympy as sp
import tool as tl
from numpy.linalg import inv

tcp_base = dt.tcp_base
camera_coordinates = dt.camera_coordinate
tcp_coordinates = dt.tcp_coordinate

# tcp_base[:,0:3] *= 0.001
# tcp_coordinates[:,0:3] *= 0.001

tcp_base_r_t_matrixs = []
tcp_base_r_t_matrix_invs = []
for i in range(tcp_base.shape[0]):
    tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_base[i,:])
    tcp_base_r_t_matrixs.append(tcp_base_r_t_matrix)
    tcp_base_r_t_matrix_invs.append(inv(tcp_base_r_t_matrix))

# print(tcp_base_r_t_matrixs)
camera_positions = np.ones((camera_coordinates.shape[0], 3), dtype=float)
for i in range(camera_coordinates.shape[0]):
    camera_positions[[i], :] = camera_coordinates[i,0:3]


print("*******************************************")
# get tcp position
tcp_positions = np.zeros((tcp_coordinates.shape[0], 6), dtype=float)
for i in range(tcp_coordinates.shape[0]):
    matrix_base = tl.getRotationAndTransferMatrix(tcp_coordinates[i, :])
    true_base = matrix_base.dot(dt.move_brush)
    # print(true_base)
    matrix_tcp = tcp_base_r_t_matrix_invs[i].dot(true_base)
    tcp_positions[i:i + 1, 0:3] = matrix_tcp[0:3, 3:4].T


tcp_data = tcp_positions[:, 0:3]
camera_data = camera_positions
# caculate
tcp_argument = np.c_[tcp_data, np.ones((tcp_data.shape[0], 1), dtype=float)]
camera_argument = np.c_[camera_data, np.ones((camera_data.shape[0], 1), dtype=float)]

selected_row = [0, 1, 2, 4]
a = sp.Matrix(camera_argument[selected_row, :])
b = sp.Matrix(tcp_argument[selected_row, :])
X = a.solve(b)
print(X.T)
############################################################
test_cameras_postions = np.ones((camera_coordinates.shape[0],3),dtype=float)
for i in range(camera_positions.shape[0]):
    test_cameras_postions[[i], :] = camera_coordinates[i,0:3]
# print(c_positions)
test_cameras_postions_argument = np.c_[test_cameras_postions, np.ones((test_cameras_postions.shape[0], 1), dtype=float)]
result = test_cameras_postions_argument.dot(X)
for i in range(result.shape[0]):
    # 创建一个对角矩阵
    diagonal_matrix = sp.diag(1, 1, 1)
    r_t_matrix = np.c_[np.r_[diagonal_matrix, np.array([[0, 0, 0]], dtype=float)], np.array([[result[i][0], result[i][1],
                                                                                              result[i][2] -200, 1.0]],
                                                                                            dtype=float).T]
    # print(np.array(tcp_base_r_t_matrix.dot(r_t_matrix)))\
    tcp_base_r_t_matrix = tcp_base_r_t_matrixs[i]
    r = np.array(tcp_base_r_t_matrix.dot(r_t_matrix))
    # print(r[:,3])


##############*******************************************
# print(result)