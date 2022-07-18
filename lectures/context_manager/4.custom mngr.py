class custom_open_file:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)
        self.mode = mode
        self.file_name = file_name

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        with open(self.file_name, 'a+') as f:
            f.seek(0)
            # print(f.read())
            # print(f.readlines()[-1])
            # print(f.tell())
            # f.readlines()
            # print(f.tell())

            if f.readlines()[-1] != 'Created by Ivan':
                f.write('\nCreated by Ivan')

            # for line in f:
            #     last_line = line
            # if last_line != 'Created by Ivan':
            #     f.write('\nCreated by Ivan')


with custom_open_file('sample.txt', 'r') as f:
    # f.write('1 new line\n')
    # f.write('2 new line\n')
    # f.write('3 new line\n')
    # f.write('4 new line\n')
    # f.write('5 new line\n')
    print(f.read())
