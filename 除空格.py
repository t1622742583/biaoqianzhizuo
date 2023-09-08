import os

in_dir = r"E:\v1.2\nofight"
for i in os.listdir(in_dir):
    os.rename(os.path.join(in_dir,i),os.path.join(in_dir,i.replace(" ","_")))