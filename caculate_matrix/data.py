"""
@Project :tool
@File    :data.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 11:07
"""
import numpy as np
# data
# tcp_base = np.array([-84.77,-340.9,609.49,0.064,-2.559,1.774])
tcp_base = np.array([150,30,450,3.0543,-1.0472,0])

data_version = 7
# ****************data_version_0*************************
camera_left_0 = np.array([
               [154,31],[361,45],[562,59],[806,80],[1043,97],
               [169,351],[354,366],[550,380],[764,392],[990,412],
               [176,595],[350,610],[534,623],[743,637],[958,654]])
camera_right_0 = np.array([
                 [61,27],[268,40],[468,53],[714,75],[954,92],
                 [85,347],[267,362],[465,376],[680,398],[906,408],
                 [97,591],[269,606],[455,619],[664,634],[878,650]])
tcp_target_modify_0 = np.array([
                     [236.52, -742.9, 545.09, 0.064, -2.559, 1.774],
                     [125.31, -742.83, 541.12, 0.064, -2.559, 1.774],
                     [13.65, -743.01, 540.32, 0.064, -2.559, 1.774],
                     [-116.84, -743.81, 535.35, 0.064, -2.559, 1.774],
                     [-252.26, -743.61, 532.49, 0.064, -2.559, 1.774],
                     [239.95, -646.53, 398.18, 0.064, -2.559, 1.774],
                     [133.63, -643.24, 392.03, 0.064, -2.559, 1.774],
                     [20.9, -643.27, 385.38, 0.064, -2.559, 1.774],
                     [-107.67, -642.8, 386.45, 0.064, -2.559, 1.774],
                     [-246.46, -642.63, 382.64, 0.064, -2.559, 1.774],
                     [243.87, -558.67, 265.31, 0.064, -2.559, 1.774],
                     [140.03, -556.04, 259.27, 0.064, -2.559, 1.774],
                     [25.27, -555.69, 255.15, 0.064, -2.559, 1.774],
                     [-105.8, -555.63, 250.91, 0.064, -2.559, 1.774],
                     [-249.91, -555.45, 245.5, 0.064, -2.559, 1.774]
                     ])
# ****************data_version_0*************************

# ****************data_version_1*************************
camera_left_1 = np.array([
               [453,42],[632,107],[829,174],[1114,287],
               [374,330],[526,414],[707,501],[941,612],
               [317,560],[451,641]])
camera_right_1 = np.array([
                 [360,36],[534,100],[724,168],[999,281],
                 [289,324],[437,409],[614,496],[838,607],
                 [240,556],[369,638]])
tcp_target_modify_1 = np.array([
                     [77.50, -746.92, 537.26, 0.064, -2.559, 1.774],
                     [-21.78, -698.75, 536.28, 0.064, -2.559, 1.774],
                     [-119.62, -651.40, 533.10, 0.064, -2.559, 1.774],
                     [-238.81, -586.67, 526.88, 0.064, -2.559, 1.774],
                     [123.29, -660.87, 393.60, 0.064, -2.559, 1.774],
                     [28.11, -611.11, 387.59, 0.064, -2.559, 1.774],
                     [-73.15, -561.98, 387.04, 0.064, -2.559, 1.774],
                     [-188.74, -504.74, 384.01, 0.064, -2.559, 1.774],
                     [162.67, -583.25, 260.48, 0.064, -2.559, 1.774],
                     [69.58, -537.25, 259.64, 0.064, -2.559, 1.774]
                     ])
# ****************data_version_1*************************

# ****************data_version_2*************************
camera_left_2 = np.array([
               [411,252],[643,350],[947,458],
               [575,536],[1187,667],
               [314,590],[541,705]])
camera_right_2 = np.array([
                 [291,244],[519,342],[810,449],
                 [458,529],[1049,660],
                 [208,583],[428,700]])
tcp_target_modify_2 = np.array([
                     [63.72, -581.66, 530.71, 0.064, -2.559, 1.774],
                     [-36.85, -540.01, 523.24, 0.064, -2.559, 1.774],
                     [-152.98, -495.10, 518.84, 0.064, -2.559, 1.774],
                     [-12.25, -495.48, 448.96, 0.064, -2.559, 1.774],
                     [-239.01, -434.51, 481.29, 0.064, -2.559, 1.774],
                     [110.75, -495.91, 386.65, 0.064, -2.559, 1.774],
                     [-1.16, -450.02, 380.31, 0.064, -2.559, 1.774]
                     ])
# ****************data_version_2*************************

# ****************data_version_3*************************
camera_left_3 = np.array([
               [643,350],
               [550,380],[1187,667],
               [314,590]])
camera_right_3 = np.array([
                 [519,342],
                 [465,376],[1049,660],
                 [208,583]])
tcp_target_modify_3 = np.array([
                     [-36.85, -540.01, 523.24, 0.064, -2.559, 1.774],
                     [20.9, -643.27, 385.38, 0.064, -2.559, 1.774],
                     [-239.01, -434.51, 481.29, 0.064, -2.559, 1.774],
                     [110.75, -495.91, 386.65, 0.064, -2.559, 1.774]
                     ])
# ****************data_version_3*************************


# ****************data_version_4*************************
camera_left_4 = np.array([
               [516,453],[633,476],[873,564],
               [609,576],
               [582,677],[574,439]])
camera_right_4 = np.array([
                 [444,449],[559,471],[789,560],
                 [533,572],
                 [505,673],[469,434]])
tcp_target_modify_4 = np.array([
                     [74.78, -791.36, 440.51, 0.064, -2.559, 1.774],
                     [-10.21, -768.67, 442.46, 0.064, -2.559, 1.774],
                     [-160.45, -711.27, 429.44, 0.064, -2.559, 1.774],
                     [3.66, -729.91, 390.23, 0.064, -2.559, 1.774],
                     [16.30, -692.52, 338.68, 0.064, -2.559, 1.774],
                     [11.78, -632.89, 557.65, 0.064, -2.559, 1.774]
                     ])
# ****************data_version_4*************************


# ****************data_version_5_ph*************************
camera_left_5 = np.array([
               [586,394],[576,549],[381,242],
               [437,224],
               [715,368],[720,259]])
camera_right_5 = np.array([
                 [472,366],[464,522],[255,210],
                 [345,211],
                 [633,357],[638,247]])
tcp_target_modify_5 = np.array([
                     [403, 75, 248, 2.879, -0.8726, 0.2617],
                     [363, 67, 195, 2.879, -0.8726, 0.2617],
                     [421, 167, 300, 2.879, -0.8726, 0.2617],
                     [535, 178, 248, 2.879, -0.8726, 0.2617],
                     [530, 8, 189, 2.879, -0.8726, 0.2617],
                     [570, 16, 241, 2.879, -0.8726, 0.2617]
                     ])
# ****************data_version_5_ph*************************

# ****************data_version_6_ph*************************
camera_left_6 = np.array([
               [486,384],[654,479],[784,494],
               [529,484],
               [564,587],[431,597]])
camera_right_6 = np.array([
                 [391,383],[565,477],[699,494],
                 [442,485],
                 [471,589],[331,599]])
tcp_target_modify_6 = np.array([
                     [653,80,305,0.0174,-1.4835,2.9671],
[641,-10,252,0.0174,-1.4835,2.9671],
[652,-88,244,0.0174,-1.4835,2.9671],
[677,55,247,0.0174,-1.4835,2.9671],
[648,37,193,0.0174,-1.4835,2.9671],
[634,107,194,0.0174,-1.4835,2.9671],
                     ])
# ****************data_version_6_ph*************************

# ****************data_version_7_ph*************************
camera_left_7 = np.array([
               [363,243],[654,203],[666,452],
               [400,358],
               [635,349],[517,252]])
camera_right_7 = np.array([
                 [261,233],[564,193],[577,446],
                 [314,351],
                 [558,342],[436,243]])
tcp_target_modify_7 = np.array([[469, 189, 447, 3.0543, -1.0472, 0],
                                [508, 25, 463, 3.0543, -1.0472, 0],
                                [428, 13, 330, 3.0543, -1.0472, 0],
                                [525, 186, 340, 3.0543, -1.0472, 0],
                                [551, 25, 333, 3.0543, -1.0472, 0],
                                [576, 111, 401, 3.0543, -1.0472, 0],
                                ])
# ****************data_version_7_ph*************************

camera_lefts = [camera_left_0,camera_left_1,camera_left_2,camera_left_3,camera_left_4,camera_left_5,camera_left_6,camera_left_7]
camera_rights = [camera_right_0,camera_right_1,camera_right_2,camera_right_3,camera_right_4,camera_right_5,camera_right_6,camera_right_7]
tcp_target_modifys = [tcp_target_modify_0,tcp_target_modify_1,tcp_target_modify_2,tcp_target_modify_3,tcp_target_modify_4,tcp_target_modify_5,tcp_target_modify_6,tcp_target_modify_7]
camera_left = camera_lefts[data_version]
camera_right = camera_rights[data_version]
tcp_target_modify = tcp_target_modifys[data_version]