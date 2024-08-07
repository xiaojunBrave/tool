"""
@Project :tool
@File    :default_test_n.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/22 14:54
"""

import data as dt
import caculate_matrix_new as cm
import tool as tl
import numpy as np
X = cm.X
move_brush = dt.move_brush.copy()
move_brush[0:3,3:4] = move_brush[0:3,3:4] * -1
t_position = dt.tcp_base_2.copy()
t_matrix = tl.getRotationAndTransferMatrix(t_position)
c_left = np.array([[488,338],[1035,485],[683,630],[616,338],[1019,445],[766,543]])
c_right = np.array([[394,303],[917,444],[571,581],[545,312],[933,415],[683,509]])
# test data
c_positions = np.ones((c_right.shape[0], 3), dtype=float)
for i in range(c_positions.shape[0]):
    x, y, z = tl.getCameraPosion(c_left[i, 0], c_left[i, 1], c_right[i, 0], c_right[i, 0])
    c_positions[[i], :] = np.array([[x, y, z]])
# print(c_positions)
c_positions_argument = np.c_[c_positions, np.ones((c_right.shape[0], 1), dtype=float)]
tcp_targets = c_positions_argument.dot(X)
# print(tcp_targets)
base_target = []
for i in range(tcp_targets.shape[0]):
    tcp = np.zeros(6,dtype=float)
    tcp[0:3] = tcp_targets[i,0:3]
    tcp_r_t = tl.getRotationAndTransferMatrix(tcp)
    result = (t_matrix.dot(tcp_r_t)).dot(move_brush)
    print(result)
    # base_target.append(result)

