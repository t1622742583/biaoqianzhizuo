import os

img_dir = r"E:\A-顶升识别\v0.1\train\wds"
val_img_dir = r"E:\A-顶升识别\v0.1\val\wds"
if not os.path.exists(val_img_dir):
    os.makedirs(val_img_dir)
for i,item in enumerate(os.listdir(img_dir)):
    if i % 7 == 0:
        img_path = os.path.join(img_dir, item)
        val_img_path = os.path.join(val_img_dir, item)
        os.rename(img_path, val_img_path)
        
        
    