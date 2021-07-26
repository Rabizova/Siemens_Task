from os import listdir


logs_path = '../logs'


def test_logs(path):
    ft_dir = listdir(path)

    if ('ft_run' not in ft_dir) or ('ft_reference' not in ft_dir):
        print('directory missing: ' + path)



directory_list = listdir(logs_path)

# print(directory_list)

for i in range(len(directory_list)):
    # print(directory_list[i])
    for directory in listdir(logs_path + '/' + directory_list[i]):
        test_logs(logs_path + '/' + directory_list[i] + '/' + directory)

