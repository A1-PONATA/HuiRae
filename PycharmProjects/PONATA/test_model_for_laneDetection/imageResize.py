import cv2
import os

'''
resize all image files to 64x64
'''

path = "/home/pirl/Documents/splited_action_data2"
save_path = "/home/pirl/Documents/splited-action-data2-modified/"
folder_list = os.listdir(path)

for d in folder_list:
    if not os.path.exists(save_path+d+'/'):
        os.mkdir(save_path+d)
    for dir in os.listdir(path+'/'+d):
        #print(dir)
        newPath = path+'/'+d+'/'+dir
        for file in os.listdir(newPath):
            filepath = newPath + "/"+file
            #print(filepath)
            img = cv2.imread(filepath, cv2.IMREAD_COLOR)
            #print(img)
            shrink = cv2.resize(img,(64,64), None, interpolation=cv2.INTER_AREA)
            print(filepath)
            cv2.imwrite(filepath, shrink)