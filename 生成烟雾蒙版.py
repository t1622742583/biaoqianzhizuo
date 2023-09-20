import random
from PIL import Image, ImageDraw, ImageFont

# 生成200张图像
def gen_mask(save_path):
    # 随机生成大小在200-500之间的数值
    size = random.randint(300, 500)
    
    # 创建一个空白图片
    image = Image.new("RGB", (512, 512), "black")
    draw = ImageDraw.Draw(image)
    
    # 使用微软雅黑字体
    font_path = "ARIBLK.TTF"  # 请确保路径正确
    font = ImageFont.truetype(font_path, size)
    
    # 随机生成S的位置
    x = random.randint(0, 512 - size)
    y = random.randint(0, 512 - size)
    align = random.choice(["right"])
    # 在图片上绘制一个大而粗的S字母
    zimu = random.choice(["C","S", "X","U","V"])
    draw.text((x, y), zimu, font=font, fill="white")
    # 
    # 保存图片，使用i作为文件名的一部分，以避免重复
    image.save(save_path)
input_dir = r"E:\yanwu\images"
save_dir = r"E:\yanwu\masks"
import os
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
# 获取images文件夹中的所有文件夹
for dir in os.listdir(input_dir):
    # 生成mask
    item_dir = os.path.join(input_dir, dir)
    save_item_dir = os.path.join(save_dir, dir)
    os.makedirs(save_item_dir, exist_ok=True)
    for file in os.listdir(item_dir):
        file = os.path.splitext(file)[0] + ".png"
        save_path = os.path.join(save_item_dir, file)
        gen_mask(save_path)
