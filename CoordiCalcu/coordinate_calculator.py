import numpy as np


# 以 origin 为中心，以 proportion 为倍率，缩放目标点 target
def zoom_by_point(target, origin, proportion):
    return (target - origin) * proportion + origin


# 沿 x 轴将目标点 target 拉伸 proportion 倍
def extrude_x(target, proportion):
    return target * np.array([proportion, 1, 1])


# 沿 y 轴将目标点 target 拉伸 proportion 倍
def extrude_y(target, proportion):
    return target * np.array([1, proportion, 1])


# 沿 z 轴将目标点 target 拉伸 proportion 倍
def extrude_z(target, proportion):
    return target * np.array([1, 1, proportion])


# 在二维平面上，将目标点 (x, y) 以坐标原点为中心逆时针旋转 r 弧度
def rotate_2d(x, y, r):
    return np.matmul([x, y], [[np.cos(r), np.sin(r)], [-np.sin(r), np.cos(r)]])


# 沿 x 坐标轴将目标点 target 旋转 degree 度
# 如果使用右手坐标系，则根据右手定则确定旋转方向
# 反之，使用左手坐标系则以左手定则确定旋转方向
# https://en.wikipedia.org/wiki/Right-hand_rule
def rotate_by_x(target, degree):
    [new_y, new_z] = rotate_2d(target[1], target[2], np.deg2rad(degree))
    return np.array([target[0], new_y, new_z])


# 沿 y 坐标轴将目标点 target 旋转 degree 度
def rotate_by_y(target, degree):
    [new_z, new_x] = rotate_2d(target[2], target[0], np.deg2rad(degree))
    return np.array([new_x, target[1], new_z])


# 沿 z 坐标轴将目标点 target 旋转 degree 度
def rotate_by_z(target, degree):
    [new_x, new_y] = rotate_2d(target[0], target[1], np.deg2rad(degree))
    return np.array([new_x, new_y, target[2]])


# 将目标点 target 沿向量 vector 平移
def move_v(target, vector):
    return target + vector


# 将目标点 target 沿方向向量 dir 平移 distance 距离
def move_d(target, dir, distance):
    dirlen = np.sqrt(np.square(dir[0]) + np.square(dir[1]) + np.square(dir[2]))
    return target + dir / dirlen * distance


# test
def test(a, b):
    print('点 a 坐标为: ' + str(a))
    print('点 b 坐标为: ' + str(b))
    print('以 b 为中心将 a 缩放 2 倍: ' + str(zoom_by_point(a, b, 2)))
    print('沿 y 轴将点 a 的坐标拉伸 2 倍: ' + str(extrude_y(a, 2)))
    print('沿 x 轴将点 a 旋转 30°: ' + str(rotate_by_x(a, 30)))
    print('沿 b 方向将点 a 移动 100 距离: ' + str(move_d(a, b, 100)))


point_a = np.array([0, 30, 90])
point_b = np.array([40, 20, 60])
# test(point_a, point_b)
print(np.linalg.norm(5, 10, 20))
print(np.sqrt(np.square(5) + np.square(10) + np.square(20)))
