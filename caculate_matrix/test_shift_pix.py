"""
@Project :tool
@File    :test_shift_pix.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 14:39
"""
import numpy as np
import tool as tl
import data as dt
import cacalate_matrix as cm
import math
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams["axes.unicode_minus"] = False
np.set_printoptions(suppress=True)
X = cm.X
t_position = dt.tcp_base.copy()
selected_index = 7
target_true_position = dt.tcp_target_modify.copy()[selected_index,:]
camera_left = dt.camera_left.copy()[selected_index,:]
camera_right = dt.camera_right.copy()[selected_index,:]

# get camera position
shift_pix = 15
shift_r = math.floor(shift_pix / 2)
# 1:往右偏移 -1往左偏移
# direction = 1
cameras_positions = np.ones((shift_pix,3),dtype=float)
for i in range(shift_pix):
    x,y,z = tl.getCameraPosion(camera_left[0], camera_left[1] + (i - shift_r), camera_right[0], camera_right[1])
    cameras_positions[[i],:] = np.array([[x,y,z]])
c_positions_argument = np.c_[cameras_positions, np.ones((shift_pix, 1), dtype=float)]
result = c_positions_argument.dot(X)
result[:,0:1] += t_position[0]
result[:,1:2] += t_position[1]
result[:,2:3] += t_position[2]
# print(result)
# draw
x = [i - shift_r for i in range(shift_pix)]
y1 = result[:,0] - target_true_position[0]
y2 = result[:,1] - target_true_position[1]
y3 = result[:,2] - target_true_position[2]
y4 = [math.sqrt(y1[i]**2 + y2[i]**2 + y3[i]**2) for i in range(shift_pix)]
# print(y1)


#折线图
def  format_spines():		# 函数: 将坐标原点设置在图中央
    ax = plt.gca()    		# gca 代表当前坐标轴
    ax.spines['right'].set_color('none')		# 隐藏坐标轴右侧边线
    ax.spines['top'].set_color('none')   		# 隐藏坐标轴顶部边线
    ax.spines['bottom'].set_position(('data', 0)) 	# 下边线移到0位置, X轴
    ax.spines['left'].set_position(('data', 0))
plt.plot(x,y1,'s-',color = 'r',label="X轴误差")#s-:方形
plt.plot(x,y2,'o-',color = 'g',label="Y轴误差")#o-:圆形
plt.plot(x,y3,'v-',color = 'b',label="Z轴误差")#v-:倒三角
plt.plot(x,y4,'p-',color = 'k',label="总误差")#v-:五角星


plt.xlabel("左右图像匹配误差/px",loc="right")#横坐标名字
plt.ylabel("成世界坐标误差/mm", loc="top")#纵坐标名字
plt.legend(loc = "lower left")#图例
plt.title("V轴方向图像匹配误差")
format_spines()
plt.show()
