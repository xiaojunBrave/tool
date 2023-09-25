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
[[-1.01066077369560, -0.0778413914959040, 0.760137939916319, 41.8723960661130],
 [-0.0458362980570345, 0.326984125381491, -1.04604641019246, 86.4773400305804],
 [0.0302563484516468, -0.960275004015696, 0.0181686728808682, 174.871838403355],
 [0, 0, 0, 1.00000000000000]]

[[-1.00845772718225, -0.0809069072825667, 0.747732117664445, 47.4936466939630],
 [-0.0467244312953509, 0.328219953334382, -1.04104514352661, 84.2111965364482],
 [0.0317502301496573, -0.962353724506119, 0.00975630814025407, 178.683597883686],
 [0, 0, 0, 1.00000000000000]]

[[-1.01243858312403, -0.0753675885891192, 0.770149161936856, 37.3361721120750],
 [-0.0474350077802276, 0.329208712953764, -1.03704373660473, 82.3981034004013],
 [0.0286238072270475, -0.958003340269126, 0.0273618588297340, 170.706277972309],
 [0, 0, 0, 1.00000000000000]]

[[-0.825834945109693, -0.200701358651232, 0.908647752610375, 22.3950306181942],
 [-0.553982467417927, 0.181455152067626, -0.514246444761828, 118.623546507635],
 [0.218067325502954, -0.827466895105855, 0.0357267363986383, 145.360013605094],
 [0, 0, 0, 1.00000000000000]]

[[-0.828493700401485, -0.203850173377824, 0.902991357260291, 26.3892283461511],
 [-0.552670839238526, 0.183008538398388, -0.511456008365554, 116.653112331064],
 [0.230781916223182, -0.812408762217112, 0.0627765186971981, 126.259124732990],
 [0, 0, 0, 1.00000000000000]]

[[-0.819013393426191, -0.192622464566645, 0.923160330485456, 12.1471426987990],
 [-0.532577177831961, 0.206805845786357, -0.468707548852512, 86.4667852989328],
 [0.228464243863103, -0.815153625906284, 0.0578457636175412, 129.740920031472],
 [0, 0, 0, 1.00000000000000]]

