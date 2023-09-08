import os

def modify_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r+") as file:
                lines = file.readlines()
                file.seek(0)  # 将文件指针移回文件开头
                for line in lines:
                    elements = line.strip().split(" ")
                    if len(elements) > 0:
                        elements[0] = "2"
                        modified_line = " ".join(elements) + "\n"
                        file.write(modified_line)
                file.truncate()  # 清除文件剩余内容（如果有）
            print(f"文件 {filename} 已成功修改。")

# 指定要修改的文件夹路径
folder_path = r"E:\A-输送管识别\42-youkoufenge_7-7_all\labels\train"

# 调用函数修改文件夹内的txt文件
modify_txt_files(folder_path)
