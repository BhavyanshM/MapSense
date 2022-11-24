import cv2
import os

class VisualSLAMDemo:

    def __init__(self) -> None:
        
        self.left_dir = "image_0"
        self.right_dir = "image_1"

        self.data_dir = '/home/quantum/Workspace/Storage/Other/Temp/dataset/sequences/00/'

        self.files = sorted(os.listdir(self.data_dir + self.left_dir))

    def run(self):

        for i in range(len(self.files)):

            print('Files:', self.files[i])

            left_img = cv2.imread(self.data_dir + self.left_dir + '/' + self.files[i])
            right_img = cv2.imread(self.data_dir + self.right_dir + '/' + self.files[i])

            cv2.imshow('Left', left_img)
            cv2.imshow('Right', right_img)

            code = cv2.waitKeyEx(1)

            if code == 113:
                exit()


if __name__ == '__main__':
    demo = VisualSLAMDemo()

    demo.run()