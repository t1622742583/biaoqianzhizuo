import os

def remove_unmatched_labels(root_folder):
    images_folder = os.path.join(root_folder, 'images')
    labels_folder = os.path.join(root_folder, 'json')

    # 获取images文件夹中的所有文件名并去掉后缀名
    image_files = set([os.path.splitext(file_name)[0] for file_name in os.listdir(images_folder)])

    # 获取labels文件夹中的所有文件名并去掉后缀名
    label_files = set([os.path.splitext(file_name)[0] for file_name in os.listdir(labels_folder)])

    # 找到在labels文件夹中存在但在images文件夹中不存在的文件
    unmatched_files = label_files - image_files

    # 删除在labels文件夹中存在但在images文件夹中不存在的文件
    for file_name in unmatched_files:
        file_path = os.path.join(labels_folder, file_name + '.json')
        os.remove(file_path)

        # 同时删除对应的图片文件
    print(f"删除了 {len(unmatched_files)} 个不匹配的文件。")

# 使用示例
root_folder = r'E:\A-输送管识别\输出管正确连接输送管连接输送管移除连接0909'  # 替换为你的根文件夹路径
remove_unmatched_labels(root_folder)
