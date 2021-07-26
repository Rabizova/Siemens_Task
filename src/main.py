from os import listdir


logs_path = '../logs'
directory_list = []


def test_logs(path):
    print('\t' + path)
    pass


for f in listdir(logs_path):
    directory_list.append(f)

print(directory_list)

for i in range(len(directory_list)):
    print(directory_list[i])

    for directory in listdir(logs_path + '/' + directory_list[i]):
        test_logs(logs_path + '/' + directory_list[i] + '/' + directory)

