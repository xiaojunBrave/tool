"""
@Project :tool
@File    :tool.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 10:40
"""
import numpy as np
import math
from scipy.spatial.transform import Rotation as R
np.set_printoptions(suppress=True)

f_carmera = 910.0
move_len = 50.0
def getCameraPosion(xl, yl, xr, yr):
    z = f_carmera * move_len / (xl - xr)
    x = xl*z / f_carmera
    y = yl*z / f_carmera
    return x,y,z


# Calculates Rotation Matrix given euler angles.
def eulerAnglesToRotationMatrix(theta):
    R_x = np.array([[1, 0, 0],
                    [0, math.cos(theta[0]), -math.sin(theta[0])],
                    [0, math.sin(theta[0]), math.cos(theta[0])]])
    # print(R_x)
    R_y = np.array([[math.cos(theta[1]), 0, math.sin(theta[1])],
                    [0, 1, 0],
                    [-math.sin(theta[1]), 0, math.cos(theta[1])]])
    # print(R_y)

    R_z = np.array([[math.cos(theta[2]), -math.sin(theta[2]), 0],
                    [math.sin(theta[2]), math.cos(theta[2]), 0],
                    [0, 0, 1]])
    # print(R_z)

    R = np.dot(R_z, np.dot(R_y, R_x))

    return R


def rotationMatrixToEulerAngles(R):

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x, y, z])

def getRotationAndTransferMatrix(postion):
    r_matrix = eulerAnglesToRotationMatrix(postion[3:6])
    r_t_matrix = np.c_[np.r_[r_matrix,np.array([[0, 0, 0]], dtype=float)], np.array([[postion[0],postion[1],
                                                                                     postion[2], 1.0]], dtype=float).T]
    return r_t_matrix

def euler2rot(euler):
    r = R.from_euler('xyz', euler, degrees=False)
    rotation_matrix = r.as_matrix()
    return rotation_matrix

def eor2euler(matrix):
    r = R.from_matrix(matrix)
    euler = r.as_euler('xyz', degrees=False)
    return euler

# print(euler2rot(np.array([-3.07759265, -0.58259265, -1.36759265])))
# print(euler2rot(np.array([0.064,-2.559,1.774])))
#
# print(eor2euler(euler2rot(np.array([0.064,-2.559,1.774]))))
# print(rotationMatrixToEulerAngles(euler2rot(np.array([0.064,-2.559,1.774]))))

shift_matrix = np.array([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,0.2],
                         [0,0,0,1]])
m = getRotationAndTransferMatrix(np.array([-0.08257,-0.32168,0.53478,0.126,-2.392,2.01 ]))
r = m.dot(shift_matrix)
print(m)
print(r)

'''
x + 100
-182.2,-326.91,541.06
Y + 100
-89.73,-304.64,436.49
z + 200
-74.40,-518.47,500.07
合
-181.23，-506.65，408.17
'''

