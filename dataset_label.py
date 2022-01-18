import glob
from PIL import Image
import shutil
import os

label_files = sorted(glob.glob("./dataset2/*"))
photo_list = []
i = 0
label_list=[" 1 0 0 0"," 0 1 0 0"," 0 0 1 0"," 0 0 0 1"]
path_w = "./list_attr_season.txt"
os.mkdir("./data_matome")

for file in label_files:
    print(file)
    photo_files = glob.glob(file + "/*")
    for photo in photo_files:
        img = Image.open(photo)
        if img.mode == 'RGB':
            photo_list.append(photo.replace(file+"/" , "")+label_list[i])
            shutil.copyfile(photo,"./data_matome/"+photo.replace(file+"/" , ""))
    i = i + 1

data_len = str(len(photo_list)) + "\n"
label_name = "spring summer autumn winter\n"
#print(photo_list)
#print(data_len)
with open(path_w, mode='w') as f:
    f.write(data_len)
    f.write(label_name)
    f.write('\n'.join(photo_list))


