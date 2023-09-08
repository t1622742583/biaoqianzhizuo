import os

# img_dir = r"E:\A-输送管识别\v0.8\cityscape\leftImg8bit\train"
# label_dir = r"E:\A-输送管识别\v0.8\cityscape\gtFine\train"
# for i,item in enumerate(os.listdir(img_dir)):
#     if i % 7 == 0:
#         img_path = os.path.join(img_dir, item)
#         os.rename(img_path, img_path.replace("train", "val"))
#         label_path = os.path.join(label_dir, item.replace(".jpg", ".json"))
#         os.rename(label_path, label_path.replace("train", "val"))
# import os

# def generate_file_list(root_dir, split):
#     image_dir = os.path.join(root_dir, 'leftImg8bit', split)
#     image_files = []

#     for file in os.listdir(image_dir):
#         if file.endswith('.png') or file.endswith('.jpg'):
#             image_files.append((os.path.join(split, file),os.path.join(split, file.replace(".jpg",".json"))))

#     return image_files

# def write_file_list(file_list, output_file):
#     with open(output_file, 'w') as f:
#         for file in file_list:
#             f.write(','.join(file) + '\n')

# # 设置Cityscapes数据集的根目录
# cityscapes_dir = r'E:\A-输送管识别\v0.8\cityscape'

# # 生成训练集的文件列表
# train_files = generate_file_list(cityscapes_dir, 'train')
# train_file_path = os.path.join(cityscapes_dir, 'train.txt')
# write_file_list(train_files, train_file_path)
# print(f"训练集文件列表已生成：{train_file_path}")

# # 生成验证集的文件列表
# val_files = generate_file_list(cityscapes_dir, 'val')
# val_file_path = os.path.join(cityscapes_dir, 'val.txt')
# write_file_list(val_files, val_file_path)
# print(f"验证集文件列表已生成：{val_file_path}")


import os

def split_dataset(root_dir, images_d, masks_d):
    images_dir = os.path.join(root_dir, images_d)
    mask_dir = os.path.join(root_dir, masks_d)
    images = sorted(os.listdir(images_dir))
    masks = sorted(os.listdir(mask_dir))

    assert len(images) == len(masks), "Number of images and masks should be the same."

    train_file = open(os.path.join(root_dir, "train.txt"), "w")
    val_file = open(os.path.join(root_dir, "val.txt"), "w")

    for i in range(len(images)):
        image_path = os.path.join(images_d, images[i])
        mask_path = os.path.join(masks_d, masks[i])

        if i % 9 == 0:
            val_file.write(f"{image_path},{mask_path}\n")
        else:
            train_file.write(f"{image_path},{mask_path}\n")

    train_file.close()
    val_file.close()

# 用法示例
root_dir = r"E:\A-输送管识别\v0.8\cityscape"
images = r"images"
masks = r"annotations"
split_dataset(root_dir,images, masks)
