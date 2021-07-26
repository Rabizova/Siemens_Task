from os import listdir
from os.path import isfile, join


my_path = '../logs'

directory_list = []

for f in listdir(my_path):
    directory_list.append(f)

print(directory_list)

for i in range(len(directory_list)):
    print(directory_list[i])

    for directory in listdir(my_path + '/' + directory_list[i]):
        print('\t' + directory)
