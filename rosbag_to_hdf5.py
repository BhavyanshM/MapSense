import rosbag
import h5py
import sys


def rosbag_info(filename):
    bag = rosbag.Bag(filename)
    print(bag._get_yaml_info())

def convert(filename, topics):
    bag = rosbag.Bag(filename)

    data = h5py.File('atlas_perception_run_1.h5', 'w')
    
    # data.create_dataset('')

    # Use ROSBag Fixer for any L515 message types that produce errors of type MsgNotFound
    # https://github.com/gavanderhoorn/rosbag_fixer

    for topic, msg, t in bag.read_messages(topics):


        if 'sensor_msgs/Image' == msg._type:
            print("Image", topic, t)  

        if 'sensor_msgs/CompressedImage' == msg._type:
            print("CompressedImage", topic, t)  

        if 'sensor_msgs/CameraInfo' == msg._type:
            print("CameraInfo", topic, t)  

        if 'sensor_msgs/CompressedImage' == msg._type:
            print("CompressedImage", topic, t)  

        if 'sensor_msgs/PointCloud2' == msg._type:
            print("PointCloud", topic, t)

        if 'sensor_msgs/Imu' == msg._type:
            print("IMU", topic, t)


    bag.close()
    data.close()

if __name__ == "__main__":
    
    path = '/home/bmishra/Workspace/Data/Atlas_Logs/ROSBags/atlas_look_and_step_01_fixed.bag'

    if len(sys.argv) > 1:
        if sys.argv[1] == 'convert':
            convert(path, [
                                '/os_cloud_node/points',
                                '/os_cloud_node/imu',
                                '/chest_l515/depth/camera_info',
                                '/chest_l515/depth/image_rect_raw'
                            ])  

        if sys.argv[1] == 'rosbag_info':
            rosbag_info(path)

        if sys.argv[1] == 'rosbag_info':
            rosbag_info(path)


    else:
        print("Provide at least 2 arguments.")


    # /chest_l515/depth/camera_info
    # /chest_l515/depth/image_rect_raw
    # /os_cloud_node/imu
    # /os_cloud_node/points