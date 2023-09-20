import os

def replace_label_ids(directory, old_label_id, new_label_id):
    # 遍历目录下的所有txt文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # 打开txt文件并读取内容
                with open(file_path, "r") as f:
                    lines = f.readlines()
                # 替换标签id并保存回txt文件
                with open(file_path, "w") as f:
                    for line in lines:
                        label_parts = line.strip().split(" ")
                        if label_parts[0] == str(old_label_id):
                            label_parts[0] = str(new_label_id)
                        f.write(" ".join(label_parts) + "\n")
                print(f"已替换标签: {file_path}")

# 指定目录路径和要替换的标签id
directory = r"E:\A-表观检测\v0.1\labels"
old_label_id = 1
new_label_id = 0

# 执行替换操作
replace_label_ids(directory, old_label_id, new_label_id)
