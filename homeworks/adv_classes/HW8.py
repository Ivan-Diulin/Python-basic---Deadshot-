# HW8 - Iterator-Generator
##########################

# 1. Implementing class iterator for Fibonacci numbers
class FibonacciNumbers:
    def __init__(self, finish_num_index):
        self.finish_num_index = finish_num_index
        if finish_num_index <= 1:
            raise Exception
        self.current_index = -1
        self.prev1_fibo_num = 0
        self.prev2_fibo_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index == 0:
            return 0
        if self.current_index == 1:
            return 1
        self.current_fibo_num = self.prev1_fibo_num + self.prev2_fibo_num
        self.prev1_fibo_num = self.prev2_fibo_num
        self.prev2_fibo_num = self.current_fibo_num
        if self.current_index > self.finish_num_index:  # exit condition
            raise StopIteration
        return self.current_fibo_num


print("1. Printing first 11 Fibonacci numbers via class iterator and for cycle:")

for i in FibonacciNumbers(10):
    print(i)


# 2. Implementing generator for Fibonacci numbers

def fibo_gen(finish_index):
    index = -1
    prev1_fibo_num = 0
    prev2_fibo_num = 1
    while True:
        index += 1
        if index > finish_index:
            return
        if index == 0:
            fibo_num = 0
        else:
            fibo_num = prev1_fibo_num + prev2_fibo_num
        prev1_fibo_num = prev2_fibo_num
        prev2_fibo_num = fibo_num
        # print(f"index={index}, fibo={fibo_num}")
        yield fibo_num


print("\n2. Printing first 11 Fibonacci numbers via generator and for cycle:")

for fn in fibo_gen(10):
    print(fn)


# 3. Implementing generator expression that returns square numbers of integers from 0 to 10

def square_gen(max_: int):
    i = 0
    while i <= max_:
        res = i**2
        i += 1
        yield res


print("\n3. Printing square numbers of integers from 0 to 10 via generator and for cycle:")

for int_ in square_gen(10):
    print(int_)


# 4.Implementing coroutine for accumulation arithmetic mean

# 4.1. Implementation using sequential operators

print("\n4.1. Printing the accumulation of arithmetic mean via coroutine."
      "\nTransferred number sequence: 2, 8, 2, 4."
      "\nResults:", end=' ')


def mean_func(prev, num):
    return round((prev+num)/2)


def accumulation_mean():

    num = yield

    mean = num
    mean = mean_func(mean, num)
    num = yield print(mean, end=', ')

    mean = mean
    mean = mean_func(mean, num)
    num = yield print(mean, end=', ')

    mean = mean
    mean = mean_func(mean, num)
    num = yield print(mean, end=', ')

    mean = mean
    mean = mean_func(mean, num)
    yield print(mean)


acc_mean = accumulation_mean()
next(acc_mean)
acc_mean.send(2)
acc_mean.send(8)
acc_mean.send(2)
acc_mean.send(4)


# 4.2. Implementation using cycles

send_list = [2, 8, 2, 4, 6, 15, 100, 47]

print("\n4.2. Printing the accumulation of arithmetic mean via coroutine + cycles."
      "\nTransferred number sequence: ", send_list,
      "\nResults:", end=' ')


def accumulation_mean_2():

    num = yield
    mean = num

    while len(send_list):
        mean = mean
        mean = mean_func(mean, num)
        num = yield print(mean, end='  ')


acc_mean_2 = accumulation_mean_2()
next(acc_mean_2)

for i in send_list:
    acc_mean_2.send(i)

print()
