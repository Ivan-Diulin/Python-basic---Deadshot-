# class ContextManager:
#     def __init__(self):
#         print('init method called')
#
#     def __enter__(self):
#         print('enter method called')
#         return self
#
#     def __exit__(self, exc_type, exc_vat, exc_tb):
#         print('exit method called')
#
#
# with ContextManager() as manager:
#     print('with statement called')


class custom_open_file:
    def __init__(self, file_name, mode='r'):
        print("Init")
        self.file = open(file_name)

    def __enter__(self):
        print('Enter')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.file.close()


with custom_open_file('sample.txt') as f:
    print("Context manager is running")
    print(f.read())

print("End")
