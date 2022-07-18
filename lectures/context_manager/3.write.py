# with open('sample.txt', 'w') as f:
#     f.write('Some new line\n')
#     f.write('And new line')

# with open('sample.txt', 'a') as f:
#     f.write('Some new line\n')
#     f.write('And new line')
#     f.write('\n NEW text')

# with open('sample.txt', 'w+') as f:
#     f.write('\n NEW TEXT')
#     f.seek(0)
#     print(f.read())

# import os - may use some os-method for faster seek of specific text | or ~regularities...

# with open('sample.txt', 'a+') as f:
#     f.write('\n NEW TEXT\n')
#     f.seek(5)  # puts cursor to defined position (the whole file is a sequence of characters with ordinal numbers)
#     # for line in f:
#     #     pass  # put cursor to some element and find/write smth
#     print(f.read())

with open('sample.txt', 'a+') as f:
    f.write('\n NEW TEXT\n')
    print(f.tell())
    print(f.read())


