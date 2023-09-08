import os
img_dir = r"E:\阀门\关闭\val\images"
label_dir = r"E:\阀门\关闭\val\labels"
for img in os.listdir(img_dir):
    img_path = os.path.join(img_dir, img)
    r_img_path = os.path.join(img_dir, "close_" + img)
    print(r_img_path)
    os.rename(img_path, r_img_path)
for label in os.listdir(label_dir):
    label_path = os.path.join(label_dir, label)
    r_label_path = os.path.join(label_dir, "close_" + label)
    print(r_label_path)
    os.rename(label_path, r_label_path)