import albumentations as A
import matplotlib.pyplot as plt
import cv2

def simulate_time_of_day(image_path, time_of_day):
    # 加载图像
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    transform = A.Compose([
        A.RandomBrightnessContrast(p=0.8), # 随机调整亮度和对比度
        A.RandomGamma(p=0.8), # 随机调整Gamma
        A.RandomBrightness( p=0.8), # 随机调整亮度
        A.CLAHE(p=0.5), # 对比度受限的自适应直方图均衡化

         A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=0, p=0.5)
        # A.HueSaturationValue(p=1, hue_shift_limit=30, sat_shift_limit=50, val_shift_limit=0),
        # A.ToFloat(),
        # ToTensorV2(),
    ])

    # 应用增强
    # transform = A.Compose(transform)
    augmented_image = transform(image=image)['image']

    # 显示原始图像和增强后的图像
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Enhanced Image ({})'.format(time_of_day.capitalize()))
    plt.imshow(augmented_image)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# 测试函数
simulate_time_of_day('ycygxl0909_26_80.jpg', 'evening')
