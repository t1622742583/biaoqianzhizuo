import json
import os
import argparse
import cv2
from tqdm import tqdm
from PIL import Image


def convert_label_txt(txt_dir, save_dir, classes):
    txt_paths = os.listdir(txt_dir)
    classes = classes.split(',')

    for txt_path in tqdm(txt_paths):
        # for txt_path in txt_paths:
        path = os.path.join(txt_dir, txt_path)
        with open(path, 'r') as load_f:
            lines = load_f.readlines()
        imagePath = f"..\\images\\{txt_path.replace('txt', 'jpg')}"
        absImagePath = os.path.abspath(os.path.join(txt_dir, imagePath))
        if not os.path.exists(absImagePath):
            print(f"文件 {absImagePath} 不存在。")
            continue
        # 使用PIL打开图片
        img = Image.open(absImagePath)
        width, height = img.size
        json_dict = {
            "version": "4.5.13",
            "flags": {}, # 
            "imageWidth": width,  # 请根据实际情况填写图像的宽度
            "imageHeight": height,  # 请根据实际情况填写图像的高度
            "shapes": [],
            "imageData": None,
            "imagePath": imagePath
        }

        for line in lines:
            line = line.strip()
            if len(line.split(' ', 1)) < 2:
                continue
            label_index, points = line.split(' ', 1)
            label_index = int(label_index)
            points = list(map(float, points.split(' ')))

            shape_dict = {
                "label": classes[label_index],
                "points": [],
                "group_id": None,
                "shape_type": "polygon",
                "flags": {}
                
            }

            for i in range(0, len(points), 2):
                x = points[i] * json_dict['imageWidth']
                y = points[i + 1] * json_dict['imageHeight']
                shape_dict['points'].append([x, y])

            json_dict['shapes'].append(shape_dict)

        # save json path
        # 不存在则创建
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        json_path = os.path.join(save_dir, txt_path.replace('txt', 'json'))
        with open(json_path, 'w') as save_f:
            json.dump(json_dict, save_f)


if __name__ == "__main__":
    """
    python txt2json.py --txt-dir my_datasets/color_rings/txts --save-dir my_datasets/color_rings/jsons --classes "cat,dogs"
    """
    classes_name = 'yeguan,qiguan,youguan'  # 中间不能带空格
    root_path = r'E:\A-输送管识别\yeguan_0908'
    parser = argparse.ArgumentParser(description='txt convert to json params')
    parser.add_argument('--txt-dir', type=str, default=rf'{root_path}\labels', help='txt path dir')
    parser.add_argument('--save-dir', type=str, default=rf'{root_path}\json', help='json save dir')
    parser.add_argument('--classes', type=str, default=classes_name, help='classes')
    parser.add_argument('--image-width', type=int, default=1920, help='image width')
    parser.add_argument('--image-height', type=int, default=1080, help='image height')
    args = parser.parse_args()
    txt_dir = args.txt_dir
    save_dir = args.save_dir
    classes = args.classes
    width = args.image_width
    height = args.image_height
    convert_label_txt(txt_dir, save_dir, classes)
