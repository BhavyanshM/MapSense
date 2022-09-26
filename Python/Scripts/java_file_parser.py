import os



count = 0
file_names = []

def extract(directory):
    global count, file_names
    
    files = os.listdir(directory)

    for file in files:

        file_path = directory + "/" + file

        if '.java' in file:
            if not('Test.java' in file):
                count+=1
                file_names.append(file)
                print(file)

        if os.path.isdir(file_path):
            extract(file_path)

def export_names(file_path, names):

    f = open(file_path, 'w+')

    for name in names:
        f.write(name + '\n')

    f.close()


if __name__ == '__main__':
    path = '/home/quantum/Workspace/Code/IHMC/repository-group/ihmc-open-robotics-software'
    output_path = '/home/quantum/Workspace/Data/Output/open-robotics-file-names.txt'

    count = 0
    file_names = []

    extract(path)

    export_names(output_path, file_names)

    print('Total Files Found:', count)

    print(file_names[:10])