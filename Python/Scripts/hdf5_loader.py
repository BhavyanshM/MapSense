import h5py
import cv2
import numpy as np

data = h5py.File('/home/quantum/Workspace/Data/Sensor_Logs/experimental.hdf5', 'r')

print(data['/d435/video/'].keys())

for i in range(len(data['/d435/video/'].keys())):

    m = data['/d435/video/' + str(i)][:].byteswap().view('uint8')
    # img = cv2.imdecode()

    print(m[-10:])

    print("Shape: ", m.shape, " DType:", m.dtype)

    image = np.asarray(m, dtype=np.uint8)


    # use imdecode function
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    print("Image: ", image.shape)


    cv2.imshow("Image", image)
    cv2.waitKey(100)