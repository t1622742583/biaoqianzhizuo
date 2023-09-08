###############################################
# 功能: 
#   1. 找出没有对应txt的jpg
#   2. 找出没有对应jpg的txt
#   3. 找出没有标签的空txt
#   1,2,3可以同时用,也可以单独使用
#   by Guo Lili 20230324
###############################################
import os
import shutil

# 1. 查找没有对应 txt 文件的 JPG
jpg_dir = r'E:/sign/person_sign/images/'             # jpg存放文件路径   E:\datasets_smoke\val_smoke_data_sys\val-5382
txt_dir = r'E:/sign/person_sign/labels/'             # txt存放文件路径
save_no_txt = r'E:/sign/txt_no/'         # 找出多余的txt文件路径
save_no_jpg = r'E:/sign/jpg_no/'         # 找出多余的jpg文件路径
save_empty_txt = r'E:/sign/txt_empty/'   # 找出空txt文件路径

if not os.path.exists(save_no_txt):
    os.makedirs(save_no_txt)
if not os.path.exists(save_no_jpg):
    os.makedirs(save_no_jpg)
if not os.path.exists(save_empty_txt):
    os.makedirs(save_empty_txt)

jpg_files = set([f[:-4] for f in os.listdir(jpg_dir) if f.endswith('.jpg')])
txt_files = set([f[:-4] for f in os.listdir(txt_dir) if f.endswith('.txt')])
missing_txt_files = jpg_files - txt_files
print(f"Missing TXT files: {len(missing_txt_files)}")
for file in missing_txt_files:
    print(file + '.jpg')
    image_jpg_path = os.path.join(jpg_dir, file + '.jpg')
    final_jpg_path = os.path.join(save_no_jpg, file + '.jpg')
    shutil.move(image_jpg_path, final_jpg_path) 

# 2. 查找没有对应 JPG 文件的 txt
# jpg_dir = 'path/to/jpg/directory'
# txt_dir = 'path/to/txt/directory'
# jpg_files = set([f[:-4] for f in os.listdir(jpg_dir) if f.endswith('.jpg')])
# txt_files = set([f[:-4] for f in os.listdir(txt_dir) if f.endswith('.txt')])
# missing_jpg_files = txt_files - jpg_files
# print(f"Missing JPG files: {len(missing_jpg_files)}")
# for file in missing_jpg_files:
#     print(file + '.txt')
#     image_txt_path = os.path.join(txt_dir, file + '.txt')
#     final_txt_path = os.path.join(save_no_txt, file + '.txt')
#     shutil.move(image_txt_path, final_txt_path) 
# 
# 3. 查找空的 txt 文件
# txt_dir = 'path/to/txt/directory'
# empty_txt_files = []
# for file in os.listdir(txt_dir):
#     if os.path.getsize(os.path.join(txt_dir, file)) == 0:
#         empty_txt_files.append(file)
# print(f"Empty TXT files: {len(empty_txt_files)}")
# for file in empty_txt_files:
#     print(file)
#     image_empty_path = os.path.join(txt_dir, file)
#     final_empty_path = os.path.join(save_empty_txt, file)
#     shutil.move(image_empty_path, final_empty_path) 
