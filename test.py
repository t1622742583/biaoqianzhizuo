import os
import json
import numpy as np
from PIL import Image
from PIL import ImageDraw
def labelme_to_cocostuff(json_path, save_dir):
    # 读取JSON文件
    with open(json_path, 'r') as f:
        data = json.load(f)

    # 创建保存目录
    os.makedirs(save_dir, exist_ok=True)

    # 获取图像宽度和高度
    img_width = data['imageWidth']
    img_height = data['imageHeight']

    # 创建空白mask图像
    mask_img = np.zeros((img_height, img_width), dtype=np.uint8)

    # 处理每个标注对象
    for shape in data['shapes']:
        # 获取标注的类别和对应的标签颜色
        label = shape['label']
        # color = shape['fill_color']

        # 获取标注的多边形区域
        polygons = shape['points']
        # polygons = json.loads(polygons)  # 将多边形坐标从字符串转换为Python对象

        mask = Image.new('L', (img_width, img_height), 0)
        ImageDraw.Draw(mask).polygon(polygons, outline=1, fill=1)

        # 将mask图像转换为numpy数组
        mask_arr = np.array(mask)

        # 根据标签颜色设置mask图像的像素值
        mask_img[mask_arr > 0] = label

    # 保存mask图像
    mask_img_path = os.path.join(save_dir, 'mask.png')
    Image.fromarray(mask_img).save(mask_img_path)

    print(f"转换完成，保存路径：{mask_img_path}")

# 示例用法
json_path = r'E:\A-输送管识别\v0.8\json\NVR_ch9_main_20230616040004_20230616050004.mp4_20230818_152559.985.json'
save_dir = '.'
labelme_to_cocostuff(json_path, save_dir)
