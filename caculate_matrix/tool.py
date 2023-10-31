"""
@Project :tool
@File    :tool.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2023/9/7 10:40
"""
import numpy as np
import math
import cv2 as cv
import data as dt
np.set_printoptions(suppress=True)
f_carmera = 910.0
move_len = 50.0
def getCameraPosion(xl, yl, xr, yr):
    '''
    双目测距
    :param xl:
    :param yl:
    :param xr:
    :param yr:
    :return:
    '''
    z = f_carmera * move_len / (xl - xr)
    x = (xl - 640)*z / f_carmera
    y = (yl - 360)*z / f_carmera
    return x,y,z
def eulerAnglesToRotationMatrix(theta):
    '''
    欧拉角（弧度）到旋转矩阵
    :param theta:
    :return:
    '''
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
    '''
    旋转矩阵转换欧拉角（弧度）
    :param R:
    :return:
    '''
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
def rotateVector2Matrix(rot_vector):
    '''
    旋转矢量转化为旋转矩阵
    :param rot_vector:
    :return:
    '''
    r = cv.Rodrigues(rot_vector)[0]
    return r
def matrxi2RotateVector(matrix):
    vec = cv.Rodrigues(matrix)[0]
    return vec
def getRotationAndTransferMatrix(postion):
    r_matrix = rotateVector2Matrix(postion[3:6])
    r_t_matrix = np.c_[np.r_[r_matrix,np.array([[0, 0, 0]], dtype=float)], np.array([[postion[0],postion[1],
                                                                                     postion[2], 1.0]], dtype=float).T]
    return r_t_matrix
'''
-0.08257,-0.32168,0.53478,0.126,-2.392,2.01 
x + 100
-182.2,-326.91,541.06
Y + 100
-89.73,-304.64,436.49
z + 200
-74.40,-518.47,500.07
合
-181.23，-506.65，408.17
'''
# tt = np.array([[1,0,0,0],
#                [0,1,0,0],
#                [0,0,1,0.2],
#                [0,0,0,1]])
# print(getRotationAndTransferMatrix(np.array([-0.08257,-0.32168,0.53478,0.126,-2.392,2.01 ])).dot(tt))



