# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 23:21
# @Author  : xiaoj
# @File    : caculate_matrix_n.py
# @Desc    :
import numpy as np
import sympy as sp
import tool as tl
import data as dt
from numpy.linalg import inv
np.set_printoptions(suppress=True)
# data
tcp_base = dt.tcp_base1.copy()
tcp_target_modify = dt.tcp_target_modify.copy()
camera_left = dt.camera_left.copy()
camera_right = dt.camera_right.copy()

tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_base)
tcp_base_r_t_matrix_inv = inv(tcp_base_r_t_matrix)

# get tcp position
tcp_targets = np.zeros((tcp_target_modify.shape[0],6),dtype=float)
for i in range(tcp_target_modify.shape[0]):
    matrix_base = tl.getRotationAndTransferMatrix(tcp_target_modify[i, :])
    # print(matrix_base)
    matrix_tcp = tcp_base_r_t_matrix_inv.dot(matrix_base)
    tcp_targets[i:i+1, 0:3] = matrix_tcp[0:3, 3:4].T

# print(tcp_targets)
# get camera position
camera_positions = np.ones((tcp_targets.shape[0], 3), dtype=float)
for i in range(tcp_targets.shape[0]):
    x,y,z = tl.getCameraPosion(camera_left[i, 0], camera_left[i, 1], camera_right[i, 0], camera_right[i, 0])
    camera_positions[[i], :] = np.array([[x, y, z]])

tcp_deta = tcp_targets[:, 0:3]
camera_targets = camera_positions
# caculate
tcp_targets_argument = np.c_[tcp_deta,np.ones((tcp_deta.shape[0],1),dtype=float)]
camera_targets_argument = np.c_[camera_targets, np.ones((camera_targets.shape[0], 1), dtype=float)]

# solve B=AX A:4x4 X:4x4 B:4x4
# 从实验数据中选取4组合适的数据

# data_0
# selected_row = [0,2,4,5]

# data_5
selected_row = [0,1,2,4]

A = sp.Matrix(camera_targets_argument[selected_row, :])
B = sp.Matrix(tcp_targets_argument[selected_row,:])
X = A.solve(B)
print(X.T)
'''
[[-0.106497160325154, -1.00773517649817, 0.642767085959976, 57.4437520379993],
 [0.957603943422352, -0.0759720891623117, -0.472737587315592, -59.0254144848690],
  [-0.213392949958245, 0.198724806697062, 1.04795938182837, -172.560867995043],
   [0, 0, 0, 1.00000000000000]]
   
[[-0.984139775154833, -0.0616359944900768, 0.748788122816705, 37.0237426342272],
 [-0.0267585438185594, 0.737800331815911, -0.964225282829529, 57.5112237559019],
  [0.0680910566678787, -0.715992435459918, -0.494403853441185, 178.557382905243],
   [0, 0, 0, 1.00000000000000]]
'''
