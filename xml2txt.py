import os
import pickle
import xml.etree.ElementTree as ET
from tqdm import tqdm

# chance your classes here
# classes= ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat',
#            'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant',
#            'sheep', 'sofa', 'train', 'tvmonitor']
# classes= ['dark_img', 'light_img_desktop',"light_img_ppt"]
classes= ['no_helmet', 'no_q_helmet',"helmet"]
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

# function:
#       (xmin, xmax, ymin, ymax) -> (center_x, cneter_y, box_weight, box_height)
# size: (w, h)
# box : (xmin, xmax, ymin, ymax)
def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0     # center_x
    y = (box[2] + box[3]) / 2.0     # center_y
    w = box[1] - box[0]             # box_weight
    h = box[3] - box[2]             # box_height
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert1(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    if w >= 1:
        w = 0.99
    if h >= 1:
        h = 0.99
    return (x, y, w, h)

# 功能：对单个文件进行转换，其中名字是相匹配的
# infile: xml文件路径
# outfile：txt文件输出路径
def convert_annotation(infile, outfile):
    in_file = open(infile, encoding='utf-8')  # xml path
    out_file = open(outfile, 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls == "oil_gloves":
            cls = "glove"
        if cls not in classes or int(difficult) == 1:   # 去掉无类别与过于困难的样本
            # print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    in_file.close()
    out_file.close()

# 功能：对xml目录下的全部xml文件全部转换成yolo的txt格式，并输出在savepath目下
# xmlpath: the dir path save xml files
# savepath: the dir path to save txt files

def xml_to_txt(xmlpath, savepath):
    assert os.path.exists(xmlpath), "{} not exists.".format(xmlpath)
    if not os.path.exists(savepath):
        os.mkdir(savepath)
        assert os.path.exists(savepath), "{} create fail.".format(savepath)
    # xmlfiles = os.listdir(xmlpath)
    # assert len(xmlfiles) != 0, "{} have no files".format(xmlpath)
    # xmlfilepaths = [os.path.join(xmlpath, xmlfile) for xmlfile in xmlfiles]
    xmlfilepaths = all_file_re_path(xmlpath, "xml")
    for xmlfilepath in tqdm(xmlfilepaths, desc="change xml to txt: "):

        image_id = xmlfilepath.split(os.sep)[-1][:-4].replace(".mp4","_mp4")
        txtfilepath = os.path.join(savepath, image_id) + ".txt"
        convert_annotation(xmlfilepath, txtfilepath)

if __name__ == '__main__':
    # VOCdevkit/VOC2012/JPEGImages
    xmlpath = r'E:\daizi_dataset\头盔未系带子(1)\头盔未系带子\xml'
    savepath = r'E:\daizi_dataset\头盔未系带子(1)\头盔未系带子\labels'
    # 创建savepath
    os.makedirs(savepath, exist_ok=True)
    xml_to_txt(xmlpath, savepath)


# 353
# 553
# 292
# tensor格式的图片合成
# import os
# import cv2
# import numpy as np
# import torch
# from PIL import Image
# from torch.utils.data import Dataset
# from torchvision import transforms
# from tqdm import tqdm
# class MyDataset(Dataset):
#
#
#
#