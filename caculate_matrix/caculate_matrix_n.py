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
# select_data_index = 2
def getA_B(select_data_index):
    camera_left = dt.camera_lefts[select_data_index].copy()
    camera_right = dt.camera_rights[select_data_index].copy()
    tcp_target_modify = dt.tcp_target_modifys[select_data_index].copy()
    tcp_base = dt.tcp_bases[select_data_index].copy()

    tcp_base_r_t_matrix = tl.getRotationAndTransferMatrix(tcp_base)
    tcp_base_r_t_matrix_inv = inv(tcp_base_r_t_matrix)

    # get tcp position
    tcp_targets = np.zeros((tcp_target_modify.shape[0], 6), dtype=float)
    for i in range(tcp_target_modify.shape[0]):
        matrix_base = tl.getRotationAndTransferMatrix(tcp_target_modify[i, :])
        true_base = matrix_base.dot(dt.move_brush)
        # print(matrix_base)
        matrix_tcp = tcp_base_r_t_matrix_inv.dot(true_base)
        tcp_targets[i:i + 1, 0:3] = matrix_tcp[0:3, 3:4].T

    # print(tcp_targets)
    # get camera position
    camera_positions = np.ones((tcp_targets.shape[0], 3), dtype=float)
    for i in range(tcp_targets.shape[0]):
        x, y, z = tl.getCameraPosion(camera_left[i, 0], camera_left[i, 1], camera_right[i, 0], camera_right[i, 0])
        camera_positions[[i], :] = np.array([[x, y, z]])

    tcp_deta = tcp_targets[:, 0:3]
    camera_targets = camera_positions
    # caculate
    tcp_targets_argument = np.c_[tcp_deta, np.ones((tcp_deta.shape[0], 1), dtype=float)]
    camera_targets_argument = np.c_[camera_targets, np.ones((camera_targets.shape[0], 1), dtype=float)]

    # print(tcp_targets_argument)
    # print(camera_targets_argument)
    # solve B=AX A:4x4 X:4x4 B:4x4
    # 从实验数据中选取4组合适的数据

    # data_0
    # selected_row = [0,2,4,5]

    # data_5
    # selected_row = [0, 1, 2, 3]
    #
    # A = sp.Matrix(camera_targets_argument[selected_row, :])
    # B = sp.Matrix(tcp_targets_argument[selected_row, :])
    # X = A.solve(B)
    # print(X.T)
    return camera_targets_argument,tcp_targets_argument

'''
[1.00951526488775, 0.00284634828765536, -0.690249743101517, -40.4702041754239],
 [0.0325109139499126, 1.00748863451193, -0.240130083583515, -164.637613307252],
  [-0.000455566454396869, -0.159240403523607, 1.05302722248871, 88.0552854774228],
   [0, 0, 0, 1.00000000000000]]
   
   [[0.975965714387571, -0.125733455789150, -0.663490602156985, -9.83177705752371],
    [0.0940068622095868, 0.822868450246127, -0.232986606245486, -158.634489866174],
     [0.274056423789449, -0.254925639662464, 0.772569741918058, 97.8185363067157], 
     [0, 0, 0, 1.00000000000000]]
     
     [[0.966791544527028, -0.136598600562092, -0.683008280937075, 3.95040459943427],
      [0.0796441182934410, 0.805858378015313, -0.263542768428798, -137.057611657713],
       [0.256101978780301, -0.276189432169859, 0.734372379574634, 124.791159053780], 
       [0, 0, 0, 1.00000000000000]]
       
       [0.966791544527028, -0.136598600562092, -0.683008280937075, 3.95040459943427], 
       [0.0796441182934410, 0.805858378015313, -0.263542768428798, -137.057611657713], 
       [0.256101978780301, -0.276189432169859, 0.734372379574634, 124.791159053780],
        [0, 0, 0, 1.00000000000000]]
'''