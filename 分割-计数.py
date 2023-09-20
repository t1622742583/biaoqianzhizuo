import os
import json

# 指定存放JSON文件的文件夹路径
folder_path = 'E:\json'
# 
# 遍历文件夹中的所有JSON文件
total_points = 0
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # 加载JSON数据
        with open(file_path) as json_file:
            data = json.load(json_file)
        
        # 计算points的数量
        for shape in data['shapes']:
            points = shape['points']
            total_points += len(points)

print("Total points:", total_points)
