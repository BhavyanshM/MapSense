import rosbag
import sys.argv


def convert(filename):
    bag = rosbag.Bag(filename)
    for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
        print(msg)
    bag.close()

if __name__ == "__main__":
    
    path = '/home/quantum/Workspace/Data/'

    if sys.argv[1] == 'convert':
        convert()