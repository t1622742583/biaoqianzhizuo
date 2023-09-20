# 划分生成训练集和验证集
import os
import random
import shutil


def split_dataset(directory, out_directory=None,train_ratio=0.8):
    if out_directory is None:
        out_directory = directory
    # 创建保存训练集和验证集的目录
    train_dir = os.path.join(out_directory, "train")
    val_dir = os.path.join(out_directory, "val")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # 获取图片文件和标注文件的路径列表
    images_dir = os.path.join(directory, "images")
    labels_dir = os.path.join(directory, "labels")
    # 不存在则创建images和labels子目录
    
    image_files = os.listdir(images_dir)
    random.shuffle(image_files)

    # 计算训练集和验证集的数量
    train_count = int(len(image_files) * train_ratio)
    val_count = len(image_files) - train_count

    # 复制训练集图片和标注文件到train目录
    for file in image_files[:train_count]:
        image_src = os.path.join(images_dir, file)
        label_src = os.path.join(labels_dir, file.split(".")[0] + ".txt")
        # 创建images和labels子目录
        os.makedirs(os.path.join(train_dir,"images"), exist_ok=True)
        os.makedirs(os.path.join(train_dir,"labels"), exist_ok=True)
        image_dst = os.path.join(train_dir,"images", file)
        label_dst = os.path.join(train_dir,"labels",file.split(".")[0] + ".txt")
        shutil.copy(image_src, image_dst)
        shutil.copy(label_src, label_dst)

    # 复制验证集图片和标注文件到val目录
    for file in image_files[train_count:]:
        image_src = os.path.join(images_dir, file)
        label_src = os.path.join(labels_dir, file.split(".")[0] + ".txt")
        os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
        os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)
        image_dst = os.path.join(val_dir,"images", file)
        label_dst = os.path.join(val_dir,"labels", file.split(".")[0] + ".txt")
        shutil.copy(image_src, image_dst)
        shutil.copy(label_src, label_dst)

    print("数据集划分完成。")
    print(f"训练集数量：{train_count}")
    print(f"验证集数量：{val_count}")

father_dir = r"E:\A-卸油基础\卸油基础模型优化0919"
abs_dir = r""
out_directory = r"E:\A-卸油基础\xieyoujiechu_dataset\v0.2"
os.makedirs(out_directory, exist_ok=True)
if father_dir != "":
    # 获取所有子目录
    sub_dirs = os.listdir(father_dir)
    # 遍历所有子目录
    for sub_dir in sub_dirs:
        # 获取子目录的路径
        sub_dir_path = os.path.join(father_dir, sub_dir)
        # 执行数据集划分操作
        split_dataset(sub_dir_path, train_ratio = 0.8,out_directory=out_directory)
else:
    split_dataset(abs_dir, train_ratio = 0.8,out_directory=out_directory)
# 获取子目录的路径
# sub_dir_path = r"E:\A-卸油基础\卸油数据\jiuJiang_618\xa_change_after_625"
# # 执行数据集划分操作
# split_dataset(sub_dir_path, train_ratio = 0.8,out_directory=r"E:\A-卸油基础\xieyoujiechu_dataset\v0.1")