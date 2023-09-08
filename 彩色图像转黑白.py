import os
import cv2
import shutil
src_dir = r"E:\oil_port_state_dataset\v0.1\val\images"
src_label_dir = r"E:\oil_port_state_dataset\v0.1\val\labels"
out_dir = r"E:\oil_port_state_dataset\v0.2\val\images"
out_label_dir = r"E:\oil_port_state_dataset\v0.2\val\labels"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
if not os.path.exists(out_label_dir):
    os.makedirs(out_label_dir)
for file in os.listdir(src_dir):
    # if file.endswith(".jpg"):
    img = cv2.imread(os.path.join(src_dir, file))
    # to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out_file_name = os.path.join(out_dir, 'gray_'+file)
    out_label_name = os.path.join(out_label_dir, 'gray_'+file.replace('.jpg', '.txt'))
    # save
    cv2.imwrite(out_file_name, img)
    # copy label
    shutil.copy(os.path.join(src_label_dir, file.replace('.jpg', '.txt')), out_label_name)

