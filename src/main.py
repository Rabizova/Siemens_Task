from os import listdir
from os.path import isfile, join


my_path = '../logs'

directory_list = []

for f in listdir(my_path):
    directory_list.append(f)

print(directory_list)
