from os import listdir
import os

logs_path = '../logs'


def test_logs(path):
    ft_dir = listdir(path)
    # local_file = open(path + '/report.txt')

    if 'ft_run' not in ft_dir:
        return ['directory missing: ft_run']
    if 'ft_reference' not in ft_dir:
        return ['directory missing: ft_reference']

    tests_dir_run = listdir(path + '/' + 'ft_run')
    tests_dir_ref = listdir(path + '/' + 'ft_reference')

    error_path_ref = []
    error_lines = []
    error_msg_ref = 'In ft_run there are missing files present in ft_reference:'
    for test in tests_dir_ref:
        if not os.path.exists(path + '/' + 'ft_run' + '/' + test):
            error_path_ref.append(path + '/' + 'ft_run' + '/' + test)

    if error_path_ref:
        error_lines.append(error_msg_ref)
        error_lines.append([str(w) + '/' + str(w) + '.stdout' for w in range(len(error_path_ref))])
        # print(error_lines)

        # asd
    error_path_run = []
    error_msg_run = 'In ft_run there are extra files not present in ft_reference:'
    for test in tests_dir_ref:
        if not os.path.exists(path + '/' + 'ft_run' + '/' + test):
            error_path_run.append(path + '/' + 'ft_run' + '/' + test)

    if error_path_run:
        error_lines.append(error_msg_run)
        error_lines.append([str(w) + '/' + str(w) + '.stdout' for w in range(len(error_path_run))])
        # print(error_lines)

    if error_lines:
        return error_lines

    return ['OK']


directory_list = listdir(logs_path)

# print(directory_list)

file = open('../reference_result.txt', 'w')

for i in range(len(directory_list)):
    if os.path.isdir(logs_path + '/' + directory_list[i]):
        for directory in listdir(logs_path + '/' + directory_list[i]):
            answer = test_logs(logs_path + '/' + directory_list[i] + '/' + directory)
            for line in answer:
                print(line)
                if line == 'OK':
                    file.write('OK: ' + directory_list[i] + '/' + directory + '/\n')
                else:
                    file.write('FAIL: ' + directory_list[i] + '/' + directory + '/\n')
                    if type(line) == type([]):
                        for a in line:
                            file.write(a)
                    else:
                        file.write(line + '\n')
file.close()
