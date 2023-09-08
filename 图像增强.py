import os
import uuid
from tqdm import tqdm
from imgaug import augmenters as iaa
import imgaug as ia
from PIL import Image
import numpy as np
sometimes = lambda aug: iaa.Sometimes(0.5, aug)
# 定义增强操作
seq = iaa.Sequential([
    iaa.Fliplr(0.5),  # 50%的概率进行水平翻转
    iaa.Flipud(0.2),  # 20%的概率进行垂直翻转
    iaa.GaussianBlur(sigma=(0, 3.0)),  # 高斯模糊，sigma值在0到3之间随机选择
    iaa.Affine(rotate=(-20, 20), shear=(-10, 10)),  # 旋转和错切变换
    iaa.AdditiveGaussianNoise(scale=(0, 0.1 * 255)),  # 添加高斯噪声，噪声强度在0到0.1之间随机选择
    # iaa.Multiply((0.8, 1.2))  # 亮度乘法，亮度因子在0.8到1.2之间随机选择
    sometimes(iaa.CropAndPad( # 裁剪图像-5%至10%的高度/宽度
            percent=(-0.05, 0.1),
            pad_mode=ia.ALL,
            pad_cval=(0, 255)
        )),
    
])
augmentations = [
    iaa.Sequential([
    iaa.Affine(rotate=(-45, 45), scale=(0.8, 1.2)),  # 随机旋转和缩放
    iaa.Fliplr(0.5),  # 随机水平翻转
    iaa.Multiply((0.8, 1.2), per_channel=0.2),  # 颜色增强
    iaa.GaussianBlur(sigma=(0.0, 3.0)),  # 模糊处理
    iaa.Crop(percent=(0.1, 0.3))  # 随机裁剪
]),
iaa.Sequential([
    iaa.Affine(rotate=(-30, 30), scale=(0.8, 1.2)),  # 随机旋转和缩放
    iaa.Fliplr(0.5),  # 随机水平翻转
    iaa.Multiply((0.8, 1.2), per_channel=0.2),  # 颜色增强
    iaa.GaussianBlur(sigma=(0.0, 1.0)),  # 模糊处理
    iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))  # 像素扰动
]),
iaa.Sequential([
    iaa.Affine(rotate=(-60, 60), scale=(0.5, 1.5)),  # 随机旋转和缩放
    iaa.Fliplr(0.5),  # 随机水平翻转
    iaa.Multiply((0.8, 1.2), per_channel=0.2),  # 颜色增强
    iaa.GaussianBlur(sigma=(0.0, 2.0)),  # 模糊处理
    iaa.SaltAndPepper(0.05)  # 椒盐噪声
])


]
# 
# 定义输入和输出文件夹的路径
src_dir = r"E:\A-顶升识别\v0.1\train\wds"  # 输入文件夹路径
out_dir = r"E:\A-顶升识别\v0.2\train\wds"  # 输出文件夹路径

# 确保输出文件夹存在
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
# 
for seq in augmentations:
    # 
    # 遍历输入文件夹中的每一个文件
    # 遍历输入文件夹中的图片文件
    for filename in tqdm(os.listdir(src_dir)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 打开图片
            image = Image.open(os.path.join(src_dir, filename))
            image_array = np.array(image)
            image_array_hwc = np.transpose(image_array, (1, 0, 2))
            img_aug = seq.augment_image(image_array_hwc)
            # 将imgaug图像转换为PIL图像
            image_aug = Image.fromarray(img_aug).convert("RGB")
            id = str(uuid.uuid1())
            image_aug.save(os.path.join(out_dir, id + ".jpg"))
            # 关闭图片
            image.close()
            image_aug.close()
