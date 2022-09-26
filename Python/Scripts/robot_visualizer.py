import h5py
import numpy as np
import matplotlib.pyplot as plt

def plot_pelvis_position(data):
    t = np.linspace(0, data.shape[0], data.shape[0])

    fig, axs = plt.subplots(3, figsize=(15,30))
    fig.suptitle('Pelvis Position Plots')

    axs[0].set_title('Pelvis Position )X')
    axs[1].set_title('Pelvis Position )X')
    axs[2].set_title('Pelvis Position )X')

    axs[0].plot(t, data[:,0], 'r-', markersize=1)
    axs[1].plot(t, data[:,1], 'r-', markersize=1)
    axs[2].plot(t, data[:,2], 'r-', markersize=1)
    plt.show()
    

def get_data(data, namespace):
    ds = []

    keys = list(map(str, sorted(list(map(int, data[namespace].keys())))))

    for key in keys:
        array = data[namespace + key][:]
        ds.append(array)

    data_block = np.vstack(ds)
    return data_block

if __name__ == '__main__':
    path = '/home/bmishra/Workspace/Data/Sensor_Logs/experimental.h5'

    data = h5py.File(path, 'r')

    
    position = get_data(data, '/robot/root/position/')
    orientation = get_data(data, '/robot/root/orientation/')
    
    joint_angles = get_data(data, '/robot/joint_angles/')
    joint_velocities = get_data(data, '/robot/joint_velocities/')
    joint_torques = get_data(data, '/robot/joint_torques/')
    
    plot_pelvis_position(position)
    # plot_joint_angles(orientation)
    # plot_joint_angles(joint_angles)
    # plot_joint_angles(joint_angles)
    # plot_joint_angles(joint_angles)
    # plot_joint_angles(joint_angles)