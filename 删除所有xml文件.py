import os
input_dir = r"E:\A-卸油基础\xieyoujiechu_dataset\v0.1\val\images"
import glob
xmls = glob.glob(os.path.join(input_dir, "*.xml"))
for xml in xmls:
    os.remove(xml)