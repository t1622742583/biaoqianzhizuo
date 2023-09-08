import os

def delete_json_files(folder_path):
    # 遍历目标文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # 检查文件是否以 .json 结尾
        if filename.endswith('.json') and os.path.isfile(file_path):
            # 删除文件
            os.remove(file_path)
            print(f"已删除文件: {filename}")

# 使用示例
target_folder = r'E:\A-输送管识别\v0.8\images'
delete_json_files(target_folder)
