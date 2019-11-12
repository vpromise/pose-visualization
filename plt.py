import numpy as np
import cv2
import os

def read_txt_file(file_path):
    image_path = []
    coord_path = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            item = line.strip().split(',')
            image_path.append(item[0])
            coord_path.append(item[1])
    return image_path, coord_path


def draw_point(img, points):
    points = points.astype(np.int)

    point_size = 1
    point_color = (0, 0, 255) # BGR
    thickness = 5

    for point_nub in range(points.shape[0]):
        # print(tuple(points[point_nub]))
        cv2.circle(img, tuple(points[point_nub]), point_size, point_color, thickness)

    # cv2.namedWindow("image_point")
    # cv2.imshow('image_point', img)
    # cv2.waitKey (10000) # 显示 10000 ms 即 10s 后消失
    # cv2.destroyAllWindows()

    return img


def draw_line(img, points):
    points = points.astype(np.int)

    point_color = (0, 255, 0) # BGR
    thickness = 2
    lineType = 8

    for point_nub in range(points.shape[0]-1):
        cv2.line(img, tuple(points[point_nub]), tuple(points[point_nub +1]), point_color, thickness, lineType)

    # cv2.namedWindow("image")
    # cv2.imshow('image', img)
    # cv2.waitKey (10000) # 显示 10000 ms 即 10s 后消失
    # cv2.destroyAllWindows()

    return img

def plt(txt_path, save_path):
    image_path, coord_path = read_txt_file(txt_path)
    for i in range(len(image_path)):
        img_path = image_path[i]
        _2d_path = coord_path[i]
        img = cv2.imread(img_path)
        _2d = np.array(np.load(_2d_path))

        img = draw_point(img, _2d)
        img = draw_line(img, _2d)
        img_save_path = save_path + "%06d" % i + ".jpg"
        cv2.imwrite(img_save_path, img)
        if i % 200 == 0:
            print("create images success")

path = "/home/vpromise/Work/Archive/video/path_128.txt"
save = "./image_128_2/"
os.makedirs(save)
plt(path, save)

