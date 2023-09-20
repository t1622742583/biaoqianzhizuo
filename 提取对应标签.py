import os
import shutil

def process_directory(root_dir, output_dir):
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)

    # 遍历根目录下的labels
    labels_dir = os.path.join(root_dir, 'labels')
    for label_file in os.listdir(labels_dir):
        if label_file.endswith('.txt'):
            with open(os.path.join(labels_dir, label_file), 'r') as f:
                lines = f.readlines()
                if any(line.startswith('1') for line in lines):
                    # 复制txt文件
                    shutil.copy(os.path.join(labels_dir, label_file), os.path.join(output_dir, 'labels'))

                    # 复制对应的图片
                    image_file = label_file.replace('.txt', '.jpg')
                    shutil.copy(os.path.join(root_dir, 'images', image_file), os.path.join(output_dir, 'images'))

                    # 修改txt文件内容，只保留以1开头的行
                    modified_lines = [line for line in lines if line.startswith('1')]
                    with open(os.path.join(output_dir, 'labels', label_file), 'w') as modified_file:
                        modified_file.writelines(modified_lines)

if __name__ == "__main__":
    root_dir = r"E:\A-卸油基础\卸油基础模型优化0917\场景5"  # 替换为你的根目录路径
    output_dir = r"E:\A-表观检测\v0.1"  # 替换为你的输出目录路径

    process_directory(root_dir, output_dir)
