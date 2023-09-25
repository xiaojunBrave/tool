"""
@Project :tool
@File    :default_test_n.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/22 14:54
"""

import data as dt
import caculate_matrix_n as cm
import tool as tl
import numpy as np
X = cm.X
t_position = dt.tcp_base.copy()
t_matrix = tl.getRotationAndTransferMatrix(t_position)
c_left = np.array([[846,462]])
c_right = np.array([[768,457]])
# test data
c_positions = np.ones((c_right.shape[0], 3), dtype=float)
for i in range(c_positions.shape[0]):
    x, y, z = tl.getCameraPosion(c_left[i, 0], c_left[i, 1], c_right[i, 0], c_right[i, 0])
    c_positions[[i], :] = np.array([[x, y, z]])
# print(c_positions)
c_positions_argument = np.c_[c_positions, np.ones((c_right.shape[0], 1), dtype=float)]
tcp_targets = c_positions_argument.dot(X)
print(tcp_targets)
base_target = []
for i in range(tcp_targets.shape[0]):
    tcp = np.zeros(6,dtype=float)
    tcp[0:3] = tcp_targets[i,0:3]
    tcp_r_t = tl.getRotationAndTransferMatrix(tcp)
    result = t_matrix.dot(tcp_r_t)
    print(result)
    # base_target.append(result)
