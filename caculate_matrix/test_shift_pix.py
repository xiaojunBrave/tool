
#!/usr/bin/env python
# coding: utf-8
import transforms3d as tfs
import numpy as np
import math

def get_matrix_eular_radu(x,y,z,rx,ry,rz):
    rmat = tfs.euler.euler2mat(math.radians(rx),math.radians(ry),math.radians(rz))
    rmat = tfs.affines.compose(np.squeeze(np.asarray((x,y,z))), rmat, [1, 1, 1])
    return rmat
def skew(v):
    return np.array([[0,-v[2],v[1]],
                     [v[2],0,-v[0]],
                     [-v[1],v[0],0]])
def rot2quat_minimal(m):
    quat =  tfs.quaternions.mat2quat(m[0:3,0:3])
    return quat[1:]

def quatMinimal2rot(q):
    p = np.dot(q.T,q)
    w = np.sqrt(np.subtract(1,p[0][0]))
    return tfs.quaternions.quat2mat([w,q[0],q[1],q[2]])

def matrix_to_eular(m):
    rx,ry,rz = tfs.euler.mat2euler(m[0:3,0:3])
    pos = np.squeeze(m[0:3,3:4])
    return (pos,math.degrees(rx),math.degrees(ry),math.degrees(rz))

hand = [1.1988093940033604, -0.42405585264804424, 0.18828251788562061, 151.3390418721659, -18.612399542280507, 153.05074895025035,
        1.1684831621733476, -0.183273375514656, 0.12744868246620855, -161.57083804238462, 9.07159838346732, 89.1641128844487,
        1.1508343174145468, -0.22694301453461405, 0.26625166858469146, 177.8815855486261, 0.8991159570568988, 77.67286224959672]

camera = [-0.15656406,  0.39817136, -0.10895333, -30.001924122750374, -51.27397651897898, 133.8490357494246,
          -0.06447235,  0.3331049 ,  0.04547163, -100.40095519488565, -3.6171481205571285, -161.84865899823535,
          -0.0781028 ,  0.46670983,  0.00937285, -90.85557233822718, 4.779633769278795, 178.99700438780516]

Hgs,Hcs = [],[]
for i in range(0,len(hand),6):
    Hgs.append(get_matrix_eular_radu(hand[i],hand[i+1],hand[i+2],hand[i+3],hand[i+4],hand[i+5]))

    m = get_matrix_eular_radu(camera[i],camera[i+1],camera[i+2],camera[i+3],camera[i+4],camera[i+5])
    m = np.linalg.inv(m)
    Hcs.append(m)
Hgijs = []
Hcijs = []
A = []
B = []
size = 0
for i in range(len(Hgs)):
    for j in range(i+1,len(Hgs)):
        size += 1
        Hgij = np.dot(np.linalg.inv(Hgs[j]),Hgs[i])
        Hgijs.append(Hgij)
        Pgij = np.dot(2,rot2quat_minimal(Hgij))

        Hcij = np.dot(Hcs[j],np.linalg.inv(Hcs[i]))
        Hcijs.append(Hcij)
        Pcij = np.dot(2,rot2quat_minimal(Hcij))

        A.append(skew(np.add(Pgij,Pcij)))
        B.append(np.subtract(Pcij,Pgij))
MA = np.asarray(A).reshape(size*3,3)
MB = np.asarray(B).reshape(size*3,1)
Pcg_  =  np.dot(np.linalg.pinv(MA),MB)
pcg_norm = np.dot(np.conjugate(Pcg_).T,Pcg_)
Pcg = np.sqrt(np.add(1,np.dot(Pcg_.T,Pcg_)))
Pcg = np.dot(np.dot(2,Pcg_),np.linalg.inv(Pcg))
Rcg = quatMinimal2rot(np.divide(Pcg,2)).reshape(3,3)

A = []
B = []
id = 0
for i in range(len(Hgs)):
    for j in range(i+1,len(Hgs)):
        Hgij = Hgijs[id]
        Hcij = Hcijs[id]
        A.append(np.subtract(Hgij[0:3,0:3],np.eye(3,3)))
        B.append(np.subtract(np.dot(Rcg,Hcij[0:3,3:4]),Hgij[0:3,3:4]))
        id += 1

MA = np.asarray(A).reshape(size*3,3)
MB = np.asarray(B).reshape(size*3,1)
Tcg = np.dot(np.linalg.pinv(MA),MB).reshape(3,)
#标记物在机械臂末端的位姿
marker_in_hand = tfs.affines.compose(Tcg,np.squeeze(Rcg),[1,1,1])

#手在眼外，标定机器人基座和相机之间的位置，这样我们就可以通过 标记物在相机的位置，相机在机械臂基坐标系的位置，求得物品在机械臂基坐标的位置
hand_in_marker = np.linalg.inv(marker_in_hand)
for i in range(len(Hgs)):
    marker_in_camera = np.linalg.inv(Hcs[i])
    base_in_hand = np.linalg.inv(Hgs[i])

    hand_in_camera = np.dot(marker_in_camera,hand_in_marker)
    base_in_camera = np.dot(hand_in_camera,base_in_hand)
    camera_in_base = np.linalg.inv(base_in_camera)
    print(camera_in_base)
#这里会输出多组数据，可以求一下均值
#这里求得的数据是相机在机械臂基坐标系中的位姿

print("SSSS")