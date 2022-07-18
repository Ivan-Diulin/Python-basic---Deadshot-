# f = open("sample.txt")
# print(f)
#
# print(f.read())
#
# c = f.read()
# print(type(c))
# #
# print(f.read(-1))
#
# print(f.readline(), end='')
# print(f.readline())
#
# for line in f:
#     print(line * 2, end='')
#
# a = f.readline()
# print(a)
# a = f.readline()
# print(a)
# a = f.readline()
# print(a)
# a = f.readline()
# print(a)
# a = f.readline()
# print(a)

# for line in f:  # work with 1 line in each iteration going through text file using readline by default
#     for i in line:  # work with each symbol of the current line from file
#         pass
#     print(line * 2, end='')
#

# print(f.fileno())  # operator which returns the descriptor of the file (number in FileHandle table of the OS)
#
# for line in f:
#     print(line * 2, end='')
#
# f.close()

# import time
#
# f = open("sample.txt")
# time.sleep(10)  # while 10 sec delay we can delete the file itself but the program will show it anyway,
#                 # because it is taken from memory using the descriptor table
# print(f.fileno())
# for line in f:
#     print(line * 2, end='')
# f.close()

# f = open("sample.txt")
# try:
#     for line in f:
#         print(line + 1)  # error with exception but file will be closed in final (independent) section
# finally:
#     f.close()

with open("sample.txt") as f:
    for line in f:
        print(line)
