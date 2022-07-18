class custom_open_file:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.mode = mode
        self.file_name = file_name

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.mode == 'r':
            self.file.seek(0)
        with open(self.file_name, 'a+') as f:
            last_line = ''
            for line in f:
                if last_line != ' ':
                    last_line = line
            print('Line', last_line, end='')
        self.file.close()


with custom_open_file('sample.txt', 'w') as f:
    f.write('1 new line')
    f.write('2 new line')
    f.write('3 new line')
    f.write('4 new line')
    f.write('5 new line')
