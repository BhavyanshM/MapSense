import h5py
import cv2
import numpy as np

data = h5py.File('/home/quantum/Workspace/Data/Sensor_Logs/experimental.hdf5', 'r')

print(data['/d435/color/'].keys())

for i in range(len(data['/d435/color/'].keys())):

    color = data['/d435/color/' + str(i)][:].byteswap().view('uint8')
    depth = data['/d435/depth/' + str(i)][:].byteswap().view('uint8')
    # img = cv2.imdecode()

    print(color[-10:])

    print("Shape: ", color.shape, " DType:", color.dtype)

    color_image = np.asarray(color, dtype=np.uint8)
    depth_image = np.asarray(depth, dtype=np.uint8)


    # use imdecode function
    color_image = cv2.imdecode(color_image, cv2.IMREAD_COLOR)
    depth_image = cv2.imdecode(depth_image, cv2.IMREAD_COLOR)

    print("Shapes: ", color_image.shape, depth_image.shape)


    cv2.imshow("color_image", color_image)
    cv2.imshow("depth_image", depth_image)
    code = cv2.waitKeyEx(30)
    if code == 113:
        exit()