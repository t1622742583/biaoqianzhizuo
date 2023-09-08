import os

img_dir = r"E:\scg\train\images"
label_dir = r"E:\scg\train\labels"

test_img_dir = r"E:\scg\val\images"
for i,item in enumerate(os.listdir(img_dir)):
    if i % 7 == 0:
        img_path = os.path.join(img_dir, item)
        iitem = item.replace(".jpg", ".txt").replace(".JPG", ".txt")
        label_path = os.path.join(label_dir, iitem)
        test_img_path = os.path.join(test_img_dir, item)
        os.rename(img_path, test_img_path)
        os.rename(label_path, label_path.replace("train", "val"))
        
    