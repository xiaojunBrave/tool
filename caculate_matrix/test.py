"""
@Project :tool
@File    :test.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 10:40
"""
import data as dt
import cacalate_matrix as cm
import tool as tl
import numpy as np
'''
X_0 = np.array([[-1.02473423803718, -0.0509350952313374, 0.0617099523589981, 0],
              [-0.0767694139150343, 0.551202034222740, -0.713368226912508, 0],
              [0.920996386906171, -0.0959745465669417, -0.378261380376526, 0],
              [-38.6420611116896, -357.726254851180, 117.864887393306, 1.00000000000000]])
'''

'''
X_1 = np.array([[-0.929568476175104, 0.134865891931638, 0.420965165617546, 0],
                [-0.0880834549834713, 0.668975611389083, -0.828043086266985, 0],
                [0.881266456231669, -0.596738691475844, 0.259990625924891, 0],
                [-42.4755653593018, -160.582557880957, -286.624330894353, 1.00000000000000]])
'''
'''
X_2 = np.array([[-0.900335573329950, 0.128466252166570, 0.221281683018763, 0],
                [-0.109574290393876, 0.649007502345485, -0.803621664254942, 0],
                [1.00382971842218, -0.491829164454619, -0.0281983300239610, 0],
                [-71.5228501916015, -143.542212221904, -19.8613142621091, 1.00000000000000]])
'''
'''
X_3 = np.array([[-0.984139775154833, -0.0267585438185594, 0.0680910566678787, 0],
                [-0.0616359944900768, 0.737800331815911, -0.715992435459918, 0],
                [0.748788122816705, -0.964225282829529, -0.494403853441185, 0],
                [37.0237426342272, 57.5112237559019, 178.557382905243, 1.00000000000000]]
)

[[-0.984139775154833, -0.0616359944900768, 0.748788122816705, 37.0237426342272],
 [-0.0267585438185594, 0.737800331815911, -0.964225282829529, 57.5112237559019],
 [0.0680910566678787, -0.715992435459918, -0.494403853441185, 178.557382905243],
 [0,                   0,                  0,                 1.00000000000000]]
'''

'''
[[-1.02146623434348, -0.0340897917782620, 0.772476019020584, 48.1375522833730],
 [-0.140171409685103, 0.522199341257993, -1.01538181589014, 77.1577765747697],
  [-0.0357183843725429, -0.827384627833558, -0.134863097492640, 189.326487127178],
   [0, 0, 0, 1.00000000000000]]
'''

'''
潘航
[[-0.0622275837084161, -0.653894999592198, 1.02043142041289, -175.286227492664],
 [-1.01268722366692, -0.185144105747728, 0.773030711565334, 23.7383961442823],
  [0.140159061638757, -0.699405975148753, -0.345565714657561, 20.7620808888940],
   [0, 0, 0, 1.00000000000000]]
   
[[-0.269922340617663, -0.801902113057610, 2.22538519053639, -581.730449702003],
 [-0.944645114683041, 0.0330287159111439, 0.409878912490794, 118.644572873398],
  [0.0244536752754198, -1.09847932093191, 0.553257262333112, 55.7723496478250],
   [0, 0, 0, 1.00000000000000]]
   
[[-0.297930666430334, -0.605071270794339, 1.51987738688197, -233.895721247723], 
[-1.12035927763002, -0.0285511274146671, 0.731790803998151, 35.3228971093836], 
[0.182874702697183, -0.940104827841319, -0.401224464286997, 255.419714993888], 
[0, 0, 0, 1.00000000000000]])
'''

X = cm.X
t_position = dt.tcp_base.copy()

# test data_flower_3
c_left = np.array([[671,612],[673,612]])
c_right = np.array([[530,603],[534,602]])
# # test data
c_positions = np.ones((c_right.shape[0],3),dtype=float)
for i in range(c_positions.shape[0]):
    x,y,z = tl.getCameraPosion(c_left[i, 0], c_left[i, 1], c_right[i, 0], c_right[i, 0])
    c_positions[[i],:] = np.array([[x,y,z]])
# print(c_positions)
c_positions_argument = np.c_[c_positions, np.ones((c_right.shape[0], 1), dtype=float)]
result = c_positions_argument.dot(X)
result[:,0:1] += t_position[0]
result[:,1:2] += t_position[1]
result[:,2:3] += t_position[2]
# print(X)
print(result)
#
# tcp_base_1 = np.array([-82.57,-321.68,534.78,0.126,-2.392,2.01])
#
# width = 1280
# height = 720
# fU_left = 0.524219 * width
# fV_left = 0.850694 * height
# fU_right = 0.414453 * width
# fV_right = 0.8375 * height
# print(fU_left, fV_left, fU_right, fV_right)
