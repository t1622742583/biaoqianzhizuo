# coding=utf8

import cv2
import os
import numpy as np
import random

import cv2
from tqdm import tqdm
 
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img
def all_file_re_path(path, fileType='jpg'):
    Dirlist = []
    Filelist = []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            if filename.split('.')[-1] == fileType:
                Filelist.append(os.path.join(home, filename))
    return Filelist

for out_size in tqdm([random.randint(100,200),random.randint(200,300),random.randint(300,400)]):
    save_idx = 0
    image_path = r"E:\A-输送管识别\输出管正确连接输送管连接输送管移除连接0906\需要裁图的\images"
    save_path = rf"E:\A-输送管识别\yeguan_0908"
    labels_path = r"E:\A-输送管识别\输出管正确连接输送管连接输送管移除连接0906\需要裁图的\labels"
    save_img_path = rf"{save_path}{os.path.sep}images"
    save_label_path = rf"{save_path}{os.path.sep}labels"
# 
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    if not os.path.exists(save_img_path):
        os.makedirs(save_img_path)
    if not os.path.exists(save_label_path):
        os.makedirs(save_label_path)
        

    label_lists = all_file_re_path(labels_path, "txt")
    print(len(label_lists))
# 
    for label in label_lists:
        label_name = os.path.basename(label)
        if label_name.startswith("xyg") or label_name.startswith("ssglj"):
            if label_name == "classes.txt":
                continue
            with open(label, "r") as read_file:
                label_infos = read_file.readlines()

            black_bottle_boxes = []
            bboxes = []
            np_bboxes = []
            for label_info in label_infos:

                points = [float(k) for k in label_info.strip().split()][1:]
                bboxes.append(points)
                np_bboxes.extend(points)

            bbboxes = np.array(np_bboxes).reshape((-1,2))

            if len(bbboxes) == 0:
                print(label)
                continue
            x1 = max(0, np.min(bbboxes[:,0]))
            x2 = min(1, np.max(bbboxes[:,0]))
            y1 = max(0, np.min(bbboxes[:,1]))
            y2 = min(1, np.max(bbboxes[:,1]))

            width = (x2 - x1)/3
            # x1向右移2个width
            if label_name.startswith("ssglj"):
                x1 = x1 + 2 * width
            elif label_name.startswith("xyg"):
                x2 = x2 - 2 * width
            
            img_filePath = os.path.join(image_path, label_name.replace(".txt", ".jpg"))
            
            img = cv_imread(img_filePath)
            H, W, C = img.shape

            org_x1 = int(x1 * W)
            org_y1 = int(y1 * H)
            org_x2 = int(x2 * W)
            org_y2 = int(y2 * H)

            pad_size_H = int(out_size * (random.randint(0,3000)/10000 + 1)) # 这里是
            pad_size_W = int(out_size * (random.randint(0,3000)/10000 + 1))
            min_size_H = int(pad_size_H * 0.05)
            min_size_W = int(pad_size_W * 0.05)

            pad_x1 = random.randint(min_size_W, pad_size_W - min_size_W)
            pad_x2 = pad_size_W - pad_x1
            pad_y1 = random.randint(min_size_H, pad_size_H - min_size_H)
            pad_y2 = pad_size_H - pad_y1

            new_x1 = max(0, org_x1 - pad_x1)
            new_x2 = min(W, org_x2 + pad_x2)
            new_y1 = max(0, org_y1 - pad_y1)
            new_y2 = min(H, org_y2 + pad_y2)

            saveImg = rf"{save_img_path}{os.path.sep}{label_name[:-4]}_{out_size}_{save_idx}.jpg"

            saveLabel = rf"{save_label_path}{os.path.sep}{label_name[:-4]}_{out_size}_{save_idx}.txt"
            temp = img[new_y1:new_y2, new_x1:new_x2]
            cv2.imencode('.jpg', temp)[1].tofile(saveImg)
            save_idx += 1

            new_h = new_y2 - new_y1
            new_w = new_x2 - new_x1

            with open(saveLabel, "w") as writeFile:
                for bb in bboxes:
                    writeFile.write(f"0")
                    bb = np.array(bb).reshape((-1,2))
                    for b in bb:
                        b[0] = ((b[0] * W) -  new_x1) / new_w
                        b[1] = ((b[1] * H) -  new_y1) / new_h
                        writeFile.write(f" {b[0]} {b[1]}")
                    writeFile.write(f"\n")