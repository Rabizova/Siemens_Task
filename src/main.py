from os import listdir
import os

logs_path = '../logs'


def test_logs(path):
    ft_dir = listdir(path)
    local_file = open(path + '/report.txt', 'w')

    if 'ft_run' not in ft_dir:
        local_file.write('directory missing: ft_run')
        local_file.close()
        return ['directory missing: ft_run']
    if 'ft_reference' not in ft_dir:
        local_file.write('directory missing: ft_reference')
        local_file.close()
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
    for test in tests_dir_run:
        if not os.path.exists(path + '/' + 'ft_run' + '/' + test):
            error_path_run.append(path + '/' + 'ft_run' + '/' + test)

    if error_path_run:
        error_lines.append(error_msg_run)
        error_lines.append([str(w) + '/' + str(w) + '.stdout' for w in range(len(error_path_run))])
        # print(error_lines)

    if error_lines:
        for error_line in answer:
            if type(error_line) == type([]):
                for word in error_line:
                    local_file.write(word)
            else:
                local_file.write(error_line + '\n')
        local_file.close()
        return error_lines

    local_file.write('OK')
    local_file.close()
    return ['OK']


directory_list = listdir(logs_path)

# print(directory_list)


for i in range(len(directory_list)):
    if os.path.isdir(logs_path + '/' + directory_list[i]):
        for directory in listdir(logs_path + '/' + directory_list[i]):
            if os.path.isdir(logs_path + '/' + directory_list[i] + '/' + directory):
                answer = test_logs(logs_path + '/' + directory_list[i] + '/' + directory)
                for line in answer:
                    if line == 'OK':
                        print('OK: ' + directory_list[i] + '/' + directory + '/\n', end='')
                    else:
                        print('FAIL: ' + directory_list[i] + '/' + directory + '/\n', end='')
                        if type(line) == type([]):
                            for a in line:
                                print(a, end='')
                        else:
                            print(line + '\n', end='')
