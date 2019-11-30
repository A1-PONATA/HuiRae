import cv2
import os

'''
resize all image files to 64x64
'''

path = "/home/pirl/Desktop/lane-4-data"
save_path = "/home/pirl/Desktop/lane-4-data-modified/"
folder_list = os.listdir(path)

for d in folder_list:
    if not os.path.exists(save_path+d+'/'):
        os.mkdir(save_path+d)
    for file in os.listdir(path+'/'+d):
        img = cv2.imread(path+'/'+d+'/'+file)
        shrink = cv2.resize(img,(64,64), None, interpolation=cv2.INTER_AREA)
        cv2.imwrite(save_path+d+'/'+file,shrink)
