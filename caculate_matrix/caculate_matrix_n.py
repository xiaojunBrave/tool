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
tcp_base = dt.tcp_base.copy()
tcp_target_modify = dt.tcp_target_modify.copy()
camera_left = dt.camera_left.copy()
camera_right = dt.camera_right.copy()

tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_base)
tcp_base_r_t_matrix_inv = inv(tcp_base_r_t_matrix)

shift_matrix = np.array([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,200],
                         [0,0,0,1]])

# get tcp position
tcp_targets = np.zeros((tcp_target_modify.shape[0],6),dtype=float)
for i in range(tcp_target_modify.shape[0]):
    matrix_base = tl.getRotationAndTransferMatrix(tcp_target_modify[i, :])
    true_base = matrix_base.dot(shift_matrix)
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

[[0.155888779407020, -0.839873031360191, 0.531803120331102, 73.0629000910348],
 [0.649253692658154, 0.138813543085990, 0.212376101067911, -152.786815743002],
 [-0.774128860093684, 0.101976010364109, 0.867757664317086, -39.5437496068747],
 [0, 0, 0, 1.00000000000000]]

[[-0.261290907119379, -0.898317049775353, 0.929064144186191, 80.7370277385512],
 [0.889204815425998, -0.00567153436724913, -0.125234996837106, -99.4024651836830],
 [-0.401522222533169, 0.483107926103972, 0.874145015286718, -157.720266669827],
 [0, 0, 0, 1.00000000000000]]