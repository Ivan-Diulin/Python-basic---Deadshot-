# HW11 - Context Manager

from datetime import datetime
import time
import csv
import json


# 1
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


print('1. File sample_0.txt:')

with open_file_logging('sample_0.txt', 'w+') as f:
    f.write('1 line\n')
    f.write('2 line\n')
    f.write('3 line\n')
    f.write('4 line\n')
    f.write('5 line\n')
    f.seek(0)
    print(f.read())
    time.sleep(1)

print('File logs.txt:')

with open('logs.txt', 'r') as f1:
    print(f1.read())


# 2
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


print('2. File logs.csv converted from logs.txt:')

log_to_csv('logs.txt', 'logs.csv')


# 3
def json_from_csv(csv_file_name: str):

    file_open_info = {
        'count': 0,
        'last_time_opened': ''
    }

    with open(csv_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for line in reader:
            if line[2] == ' Open':
                file_open_info['count'] += 1
                file_open_info['last_time_opened'] = line[0]

        file_open_dict = {'sample_0.txt': file_open_info}

        with open('open_log.json', 'w') as json_file:
            json.dump(file_open_dict, json_file, indent=4)


json_from_csv('logs.csv')

print('3. File open_log.json with data gathered from logs.csv:')

with open('open_log.json', 'r') as file:
    print(json.load(file))
