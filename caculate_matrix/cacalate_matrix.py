"""
@Project :tool
@File    :cacalate_matrix.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 10:39
"""
import numpy as np
import sympy as sp
import tool as tl
import data as dt
np.set_printoptions(suppress=True)
# data
tcp_base = dt.tcp_base.copy()
tcp_target_modify = dt.tcp_target_modify.copy()
camera_left = dt.camera_left.copy()
camera_right = dt.camera_right.copy()

# get tcp position
tcp_target_modify[:,0:1] -= tcp_base[0]
tcp_target_modify[:,1:2] -= tcp_base[1]
tcp_target_modify[:,2:3] -= tcp_base[2]

# get camera position
camera_positions = np.ones((tcp_target_modify.shape[0], 3), dtype=float)
for i in range(tcp_target_modify.shape[0]):
    x,y,z = tl.getCameraPosion(camera_left[i, 0], camera_left[i, 1], camera_right[i, 0], camera_right[i, 0])
    camera_positions[[i], :] = np.array([[x, y, z]])

tcp_deta = tcp_target_modify[:, 0:3]
camera_targets = camera_positions
# caculate
tcp_targets_argument = np.c_[tcp_deta,np.ones((tcp_deta.shape[0],1),dtype=float)]
camera_targets_argument = np.c_[camera_targets, np.ones((camera_targets.shape[0], 1), dtype=float)]

# solve B=AX A:4x4 X:4x4 B:4x4
# 从实验数据中选取4组合适的数据

# data_0
# selected_row = [0,2,4,5]

# data_5
selected_row = [0,1,2,3]

A = sp.Matrix(camera_targets_argument[selected_row, :])
B = sp.Matrix(tcp_targets_argument[selected_row,:])
X = A.solve(B)
print(X.T)


