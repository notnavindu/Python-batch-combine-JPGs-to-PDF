import os
from PIL import Image

# absolute path
d = raw_input("Enter absolute directory path: ")
imageList = []

for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        print(full_path)
        image1 = Image.open(full_path)
        im1 = image1.convert('RGB')
        imageList.append(im1)

imageList[0].save(d, save_all=True, append_images=imageList[1:])