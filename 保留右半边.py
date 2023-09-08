from PIL import Image
import os

def split_and_save_images(folder_path,output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 获取目标文件夹内所有文件
    file_list = os.listdir(folder_path)

    # 循环处理每个文件
    for file_name in file_list:
        # 检查文件是否为图片文件
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # 拼接图片文件的完整路径
            file_path = os.path.join(folder_path, file_name)

            # 读取图片文件
            image = Image.open(file_path)

            # 获取图片的宽度和高度
            width, height = image.size

            # 计算分割点
            split_point = width // 2

            # 分割图片并保留右边部分
            right_half_image = image.crop((split_point, 0, width, height))

            # 保存分割后的图片
            save_path = os.path.join(output_dir, file_name)
            right_half_image.save(save_path)

            # 关闭当前图片
            image.close()

# 指定目标文件夹路径
folder_path = r'E:\A-输送管识别\youbanbian'
output_dir = r'E:\A-输送管识别\right_half'
# 调用函数进行图片处理
split_and_save_images(folder_path,output_dir)
