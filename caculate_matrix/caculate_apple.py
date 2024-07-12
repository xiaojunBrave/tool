'''
在执行手眼标定时，需要将标定板放置某一固定位置，并同时将相机固定在机械臂末端。
接着控制机械臂末端位于不同的位置，记录下此时机械臂相对于基座的位姿，并使用相机拍摄标定板上的棋盘格图像。
将图像放入./images文件夹中，并将位姿信息输入到chessboard_handeye_calibration.py文件的pose_vectors变量中。
最后运行chessboard_handeye_calibration.py，即可得到相机相对于机械臂末端的位姿矩阵。
'''

import cv2
import numpy as np
import transforms3d
import glob

def pose_vectors_to_end2base_transforms(pose_vectors):
    # 提取旋转矩阵和平移向量
    R_end2bases = []
    t_end2bases = []

    # 迭代遍历每个位姿的旋转矩阵和平移向量
    for pose_vector in pose_vectors:
        # 提取旋转矩阵和平移向量
        R_end2base = euler_to_rotation_matrix(pose_vector[3], pose_vector[4], pose_vector[5])
        t_end2base = pose_vector[:3]

        # 提取旋转矩阵和平移向量
        R_end2bases.append(R_end2base)
        t_end2bases.append(t_end2base)

    return R_end2bases, t_end2bases

def euler_to_rotation_matrix(rx, ry, rz, unit='rad'):  # rx, ry, rz是欧拉角，单位是度
    '''
    将欧拉角转换为旋转矩阵：R = Rz * Ry * Rx
    :param rx: x轴旋转角度
    :param ry: y轴旋转角度
    :param rz: z轴旋转角度
    :param unit: 角度单位，'deg'表示角度，'rad'表示弧度
    :return: 旋转矩阵
    '''
    if unit =='deg':
        # 把角度转换为弧度
        rx = np.radians(rx)
        ry = np.radians(ry)
        rz = np.radians(rz)

    # 计算旋转矩阵Rz 、 Ry 、 Rx
    Rx = transforms3d.axangles.axangle2mat([1, 0, 0], rx)
    Ry = transforms3d.axangles.axangle2mat([0, 1, 0], ry)
    Rz = transforms3d.axangles.axangle2mat([0, 0, 1], rz)

    # 计算旋转矩阵R = Rz * Ry * Rx
    rotation_matrix = np.dot(Rz, np.dot(Ry, Rx))

    return rotation_matrix

#################### 输入 ##########################################################################################################
# 输入位姿数据，注意欧拉角是角度还是弧度
pose_vectors = np.array([
[-0.1431792323746138, -0.40360889689561186, 0.47770592772534276, -1.5734139710501989, 2.409593533216064, -0.42271422074517184],
[-0.10558645849063232, -0.36485879267571175, 0.4777075842162012, -0.955770604644236, 2.8505336197403692, -0.5250474080288211],
[-0.055605085108585396, -0.3343521068951687, 0.4777363692345726, -0.2686891548153627, 3.0735612672470882, -0.5569312228477132],
[0.049783381478276795, -0.31332071962187213, 0.4777284566920419, -0.8835643874644553, -2.8365630484873345, 0.49980874257440344],
[0.15713640165277873, -0.38516338616256984, 0.47773840453702326, -1.789798338140261, -2.2510776341159744, 0.3831720676742557],
[0.13769303622687534, -0.4995259161819387, 0.4592511394740081, -1.637661000875005, -2.4142989255824423, 0.1746919013851672],
[-0.23944466180606805, -0.5883495633798423, 0.4592166932682419, 1.5668530945590458, 2.3292941253540236, 0.34340020782307956],
[0.24377097017855692, -0.535659228941653, 0.4591830241531807, -1.1762304770801038, -2.5344009967586585, 0.2583010248676246],
[-0.08063285900502719, -0.37753164323435046, 0.4592290988391119, 1.0454700264418304, 2.722706144854548, -0.22596636527451763],
[-0.18566292979555638, -0.36673109673515886, 0.4592473553247933, 1.014793217342478, 2.5669904620308137, -0.1282114540725322],
[-0.3244291990941228, -0.36675146368799605, 0.45921955676308546, 0.9659099352963033, 2.3454278279712746, -0.003163362125228643],
[-0.3817760288349301, -0.3034033505271504, 0.45922991183286227, 0.7865206236956784, 2.240895750907218, -0.4079941672029053],
[0.48224528509483255, -0.2150472710170148, 0.4592139890084022, -0.3065356065830922, -2.281436461347898, 0.8316840023457838],
[0.48221661813369865, -0.2150480520775736, 0.45921873146912334, -0.40985599089344477, -2.4730441848816294, 0.8333332760371784],
[0.48222680481375096, -0.21501977349757623, 0.45918514729065496, -0.3455332094911811, -2.5213573977481296, 0.6050863783579159],
[0.4822276468477533, -0.32662783628565184, 0.45923944994824933, -0.8082324619909051, -2.3446577143827945, 0.5318509686183843],
[0.3506668046327158, -0.3265983073919549, 0.45920902280901027, -0.9525908921663911, -2.5208749320317683, 0.6647610939577269],
[0.021847831209150056, -0.39786644836519547, 0.4496902166105174, -0.12699800792743998, -3.0892328757236136, 0.3770781308634998],
 [-0.08424375069542596, -0.3034038406286113, 0.44975665037442847, -0.134110150095713, -3.030043770838248, 0.7706464971770348],
  [-0.3639155019120924, -0.30342717516782525, 0.44970164514610184, 0.348234614739415, 2.286797835843926, -0.5367602979895996],
 [0.3042657766330837, -0.30343393855716716, 0.44972915171554834, 0.00959923196975673, -2.410646821010541, 0.6056400579748094],
 [0.04908782907834175, -0.5910427651133767, 0.4497050297643798, -0.12238390299505345, -3.0470351355095984, -0.21679836516532827],
 [0.04907942586906755, -0.6782392253295074, 0.4497300087299408, -0.1144937260843069, -3.024589908790772, -0.3961430706002463],
 [-0.3385255115432567, -0.5334017549410403, 0.44972545076985615, -0.13719334784255555, 2.689002263939641, 0.06768650720551171],
  [0.1277461102168353, -0.40357792682510907, 0.4497643249351853, -1.4455310901268292, -2.5590703252460587, 0.3843614186072293],
  [-0.08502290482977308, -0.4035618094404585, 0.44975058123537637, -1.5250904232770233, 2.575269886081319, -0.32914612259562254],
  [-0.3286077709455036, -0.4035702936899082, 0.4497111673883375, -1.3567652238194496, 2.195761927692097, -0.5923982707236287],
  [-0.19896401137233574, -0.4035897691049425, 0.4497098399252627, -1.5148723041922851, 2.382971304330613, -0.4766712657254315]
])

# pose_vectors = np.array([[0.021847831209150056, -0.39786644836519547, 0.4496902166105174, -0.12699800792743998, -3.0892328757236136, 0.3770781308634998],
#  [-0.08424375069542596, -0.3034038406286113, 0.44975665037442847, -0.134110150095713, -3.030043770838248, 0.7706464971770348],
#   [-0.3639155019120924, -0.30342717516782525, 0.44970164514610184, 0.348234614739415, 2.286797835843926, -0.5367602979895996],
#  [0.3042657766330837, -0.30343393855716716, 0.44972915171554834, 0.00959923196975673, -2.410646821010541, 0.6056400579748094],
#  [0.04908782907834175, -0.5910427651133767, 0.4497050297643798, -0.12238390299505345, -3.0470351355095984, -0.21679836516532827],
#  [0.04907942586906755, -0.6782392253295074, 0.4497300087299408, -0.1144937260843069, -3.024589908790772, -0.3961430706002463],
#  [-0.3385255115432567, -0.5334017549410403, 0.44972545076985615, -0.13719334784255555, 2.689002263939641, 0.06768650720551171],
#   [0.1277461102168353, -0.40357792682510907, 0.4497643249351853, -1.4455310901268292, -2.5590703252460587, 0.3843614186072293],
#   [-0.08502290482977308, -0.4035618094404585, 0.44975058123537637, -1.5250904232770233, 2.575269886081319, -0.32914612259562254],
#   [-0.3286077709455036, -0.4035702936899082, 0.4497111673883375, -1.3567652238194496, 2.195761927692097, -0.5923982707236287],
#   [-0.19896401137233574, -0.4035897691049425, 0.4497098399252627, -1.5148723041922851, 2.382971304330613, -0.4766712657254315]])

# 定义棋盘格参数
square_size = 30.0  # 假设格子的边长为30mm
pattern_size = (7, 5)   # 在这个例子中，假设标定板有9个内角点和6个内角点

# 导入相机内参和畸变参数
# 焦距 fx, fy, 光心 cx, cy
# 畸变系数 k1, k2
fx, fy, cx, cy = 588.689424, 591.301662, 313.812757, 247.774261
k1, k2 = 0.075547, -0.158087
K = np.array([[fx, 0, cx],
              [0, fy, cy],
              [0, 0, 1]], dtype=np.float64)   # K为相机内参矩阵
dist_coeffs = np.array([k1, k2, 0, 0], dtype=np.float64)   # 畸变系数

# 所有图像的路径
images = glob.glob('D:\\Desktop\\t1\\*.jpg')
###########################################################################################################################


# 准备位姿数据
obj_points = []  # 用于保存世界坐标系中的三维点
img_points = []  # 用于保存图像平面上的二维点

# 创建棋盘格3D坐标
objp = np.zeros((np.prod(pattern_size), 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size


# 迭代处理图像
det_success_num = 0  # 用于保存检测成功的图像数量
for image in images:
  img = cv2.imread(image)   # 读取图像
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # RGB图像转换为灰度图像

  # 棋盘格检测
  ret, corners = cv2.findChessboardCorners(gray, pattern_size)

  if ret:
    det_success_num += 1
    # 如果成功检测到棋盘格，添加图像平面上的二维点和世界坐标系中的三维点到列表
    obj_points.append(objp)
    img_points.append(corners)

    # 绘制并显示角点
    cv2.drawChessboardCorners(img, pattern_size, corners, ret)
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 640, 480)
    cv2.imshow('img', img)
    cv2.waitKey(500)

cv2.destroyAllWindows()

# # 打印obj_point和img_point的形状
# print(np.array(obj_points).shape)
# print(np.array(img_points).shape)


# 求解标定板位姿
R_board2cameras = []  # 用于保存旋转矩阵
t_board2cameras = []  # 用于保存平移向量
# 迭代的到每张图片相对于相机的位姿
for i in range(det_success_num):
  # rvec：标定板相对于相机坐标系的旋转向量
  # t_board2camera：标定板相对于相机坐标系的平移向量
  ret, rvec, t_board2camera = cv2.solvePnP(obj_points[i], img_points[i], K, dist_coeffs)

  # 将旋转向量(rvec)转换为旋转矩阵
  # R：标定板相对于相机坐标系的旋转矩阵
  R_board2camera, _ = cv2.Rodrigues(rvec)   # 输出：R为旋转矩阵和旋转向量的关系  输入：rvec为旋转向量

  # 将标定板相对于相机坐标系的旋转矩阵和平移向量保存到列表
  R_board2cameras.append(R_board2camera)
  t_board2cameras.append(t_board2camera)

# # 打印R_board2cameras和t_board2cameras的形状
# print(np.array(R_board2cameras).shape)
# print(np.array(t_board2cameras).shape)

# 求解手眼标定
# R_end2bases：机械臂末端相对于机械臂基座的旋转矩阵
# t_end2bases：机械臂末端相对于机械臂基座的平移向量
R_end2bases, t_end2bases = pose_vectors_to_end2base_transforms(pose_vectors)

# R_camera2end：相机相对于机械臂末端的旋转矩阵
# t_camera2end：相机相对于机械臂末端的平移向量
R_camera2end, t_camera2end = cv2.calibrateHandEye(R_end2bases, t_end2bases,
                                                    R_board2cameras, t_board2cameras,
                                                    method=cv2.CALIB_HAND_EYE_TSAI)

# 将旋转矩阵和平移向量组合成齐次位姿矩阵
T_camera2end = np.eye(4)
T_camera2end[:3, :3] = R_camera2end
T_camera2end[:3, 3] = t_camera2end.reshape(3)

# 输出相机相对于机械臂末端的旋转矩阵和平移向量
print("Camera to end rotation matrix:")
print(R_camera2end)
print("Camera to end translation vector:")
print(t_camera2end)

# 输出相机相对于机械臂末端的位姿矩阵
print("Camera to end pose matrix:")
np.set_printoptions(suppress=True)  # suppress参数用于禁用科学计数法
print(T_camera2end)