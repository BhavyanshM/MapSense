import cv2
import os

path = '/home/quantum/Workspace/Storage/Other/Temp/dataset/sequences/00/image_0/'

files = sorted(os.listdir(path))

for i in range(len(files)):

    print('Files:', files[i])

    img = cv2.imread(path + files[i])

    cv2.imshow('Window', img)

    code = cv2.waitKeyEx(1)

    if code == 113:
        exit()