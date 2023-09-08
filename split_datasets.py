# 将图片和标注数据按比例切分为 训练集和测试集
import shutil
import random
import os
import argparse


# 检查文件夹是否存在
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main(image_dir, txt_dir, save_dir):
    # 创建文件夹
    mkdir(save_dir)
    images_dir = os.path.join(save_dir, 'images')
    labels_dir = os.path.join(save_dir, 'labels')

    img_train_path = os.path.join(images_dir, 'train')
    img_val_path = os.path.join(images_dir, 'val')

    label_train_path = os.path.join(labels_dir, 'train')
    label_val_path = os.path.join(labels_dir, 'val')

    mkdir(images_dir)
    mkdir(labels_dir)
    mkdir(img_train_path)
    mkdir(img_val_path)
    mkdir(label_train_path)
    mkdir(label_val_path)

    # 数据集划分比例，训练集80%，验证集20%，按需修改
    train_percent = 0.8

    total_txt = os.listdir(txt_dir)
    num_txt = len(total_txt)
    list_all_txt = list(range(num_txt))  # 范围 list(range(0, num))

    num_train = int(num_txt * train_percent)
    train = random.sample(list_all_txt, num_train)
    val = [i for i in list_all_txt if i not in train]

    print("训练集数目：{}, 验证集数目：{}".format(len(train), len(val)))
    for i in list_all_txt:
        name = total_txt[i][:-4]

        srcImage = os.path.join(image_dir, name + '.jpg')
        srcLabel = os.path.join(txt_dir, name + '.txt')

        if i in train:
            dst_train_Image = os.path.join(img_train_path, name + '.jpg')
            dst_train_Label = os.path.join(label_train_path, name + '.txt')
            shutil.copyfile(srcImage, dst_train_Image)
            shutil.copyfile(srcLabel, dst_train_Label)
        else:
            dst_val_Image = os.path.join(img_val_path, name + '.jpg')
            dst_val_Label = os.path.join(label_val_path, name + '.txt')
            shutil.copyfile(srcImage, dst_val_Image)
            shutil.copyfile(srcLabel, dst_val_Label)
if __name__ == '__main__':
    """
    python split_datasets.py --image-dir my_datasets/color_rings/imgs --txt-dir my_datasets/color_rings/txts --save-dir my_datasets/color_rings/train_data
    """
    parser = argparse.ArgumentParser(description='split datasets to train,val,test params')
    parser.add_argument('--image-dir', type=str, default=r'E:\A-输送管识别\输出管正确连接输送管连接输送管移除连接0825第一份\images', help='image path dir')
    parser.add_argument('--txt-dir', type=str, default=r'E:\A-输送管识别\输出管正确连接输送管连接输送管移除连接0825第一份\labels', help='txt path dir')
    parser.add_argument('--save-dir', default=r'E:\A-输送管识别\v0.6', type=str, help='save dir')
    args = parser.parse_args()
    image_dir = args.image_dir
    txt_dir = args.txt_dir
    save_dir = args.save_dir
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    main(image_dir, txt_dir, save_dir)

