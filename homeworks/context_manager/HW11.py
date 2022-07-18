from datetime import datetime
import time
import csv
import json


class open_file_logging:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = open(file_name, mode)
        with open('logs.txt', 'a') as log_file:
            str_ = str(datetime.now())+' '+file_name+' Open\n'
            log_file.write(str_)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        with open('logs.txt', 'a') as log_file:
            msg = str(datetime.now())+' '+self.file_name+' Close\n'
            log_file.write(msg)


with open_file_logging('sample_0.txt', 'w+') as f:
    f.write('1 line\n')
    f.write('2 line\n')
    f.write('3 line\n')
    f.write('4 line\n')
    f.write('5 line\n')
    f.seek(0)
    print(f.read())
    time.sleep(1)


def log_to_csv(log_file_name: str, csv_file_name: str):

    with open(csv_file_name, 'w') as csv_file:
        pass

    with open(log_file_name, 'r') as log_file:
        for line in log_file:
            line_list = list(line.split(' '))
            line_list[0] = line_list[0] + ' ' + line_list.pop(1)
            line_list[1] = ' ' + line_list[1]
            line_list[2] = ' ' + line_list[2]
            line_list[2] = line_list[2].replace('\n', '')
            with open(csv_file_name, 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(line_list)
    with open(csv_file_name, 'r') as csv_file:
        csv_file.seek(0)
        print(csv_file.read())


log_to_csv('logs.txt', 'logs.csv')


def json_from_csv(csv_file_name: str):

    file_open_info = {
        'count': 0,
        'last_time_opened': ''
    }

    count = 0
    last_time_opened = ''

    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            if line[2] == ' Open':
                file_open_info['count'] += 1
                file_open_info['last_time_opened'] = line[0]

            print(line, type(line))

        print(count, last_time_opened)

        file_open_dict = {'sample_0.txt': file_open_info}

        with open('open_log.json', 'w') as json_file:
            json.dump(file_open_dict, json_file, indent=4)


json_from_csv('logs.csv')



# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE

# TASK 2
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE

# TASK 3 (з зірочкою)
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }


# P.S. Якщо щось не зрозуміло по умові задачі, то робіть як вважаєте за доцільно,
# користуючись здоровим глуздом звичайно ж)
