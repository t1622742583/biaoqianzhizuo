import os
import random

data_dir = r'E:\v1.2'
train_list = []
test_list = []

# 遍历正样本文件夹
fight_dir = os.path.join(data_dir, 'fight')
fight_list = os.listdir(fight_dir)
fight_num = len(fight_list)
fight_train_num = int(fight_num * 0.8)
fight_test_num = fight_num - fight_train_num
# 随机打乱文件列表
random.shuffle(fight_list)
# 将训练集和测试集的文件路径写入train_list.txt和test_list.txt文件中
for file_name in fight_list[:fight_train_num]:
    nn = os.path.relpath(os.path.join(fight_dir, file_name), data_dir)
    nn = nn.replace('\\', '/')
    train_list.append(nn + ' 1\n')
for file_name in fight_list[fight_train_num:]:
    nn = os.path.relpath(os.path.join(fight_dir, file_name), data_dir)
    nn = nn.replace('\\', '/')
    test_list.append(nn + ' 1\n')

# 遍历负样本文件夹
nofight_dir = os.path.join(data_dir, 'nofight')
nofight_list = os.listdir(nofight_dir)
nofight_num = len(nofight_list)
nofight_train_num = int(nofight_num * 0.8)
nofight_test_num = nofight_num - nofight_train_num
# 随机打乱文件列表
random.shuffle(nofight_list)
# 将训练集和测试集的文件路径写入train_list.txt和test_list.txt文件中
for file_name in nofight_list[:nofight_train_num]:
    nn = os.path.relpath(os.path.join(nofight_dir, file_name), data_dir)
    nn = nn.replace('\\', '/')
    train_list.append(nn + ' 0\n')
for file_name in nofight_list[nofight_train_num:]:
    nn = os.path.relpath(os.path.join(nofight_dir, file_name), data_dir)
    nn = nn.replace('\\', '/')
    test_list.append(nn + ' 0\n')

# 将结果写入文件
with open(os.path.join(data_dir, 'train_list.txt'), 'w', encoding='utf-8') as f_train:
    f_train.writelines(train_list)
with open(os.path.join(data_dir, 'val_list.txt'), 'w', encoding='utf-8') as f_test:
    f_test.writelines(test_list)
