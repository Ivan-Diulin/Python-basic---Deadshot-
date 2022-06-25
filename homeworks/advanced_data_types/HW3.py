##################################################
#Homework 3 by Ivan Diulin, 2022.06.24
##################################################

#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("1.")
print("ID of 'int_a':", id(int_a))
print("ID of 'str_b':", id(str_b))
print("ID of 'set_c':", id(set_c))
print("ID of 'lst_d':", id(lst_d))
print("ID of 'dict_e':", id(dict_e))
#  Note: IDs are subjects to change on every run of this py script

##################################################

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print("2.")
print("ID of 'lst_d' after 2 appends:", id(lst_d)) # after 2 appends id of this list remains the same

##################################################

# 3. Define the type of each object from step 1.
print("3.")
print("Type of 'int_a':", type(int_a))
print("Type of 'str_b':", type(str_b))
print("Type of 'set_c':", type(set_c))
print("Type of 'lst_d':", type(lst_d))
print("Type of 'dict_e':", type(dict_e))

##################################################

# 4*. Check the type of the objects by using isinstance.
py_types = (str, int, float, complex, list, tuple, range,
              dict, set, frozenset, bool, bytes, bytearray,
              memoryview, None)
def check_type (var):
    for i in py_types:
        if isinstance(var, i) == True:
            return i
print("4.")
print("Variable 'int_a' is of type:", check_type(int_a))
print("Variable 'str_b' is of type:", check_type(str_b))
print("Variable 'set_c' is of type:", check_type(set_c))
print("Variable 'lst_d' is of type:", check_type(lst_d))
print("Variable 'dict_e' is of type:", check_type(dict_e))

##################################################

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("5.")
print("Anna has {} apples and {} peaches.".format(3, 5))

##################################################

# 6. By passing index numbers into the curly braces.
print("6.")
print("Anna has {1} apples and {0} peaches.".format(3, 5))

##################################################

# 7. By using keyword arguments into the curly braces.
print("7.")
print("Anna has {num_apples} apples and {num_peaches} peaches.".format(num_apples="three", num_peaches="five"))

##################################################

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("8.")
print("Anna has {num_apples:5} apples and {num_peaches:3} peaches.".format(num_apples=5, num_peaches=3))

##################################################

# 9. With f-strings and variables
print("9.")
num_apples = 3
num_peaches = "five"
print(f"Anna has {num_apples} apples and {num_peaches} peaches.")

##################################################

# 10. With % operator
print("10.")
num_apples = "three"
print("Anna has %s apples" % num_apples + " and %s peaches." % num_peaches)

##################################################

# 11*. With variable substitutions by name (hint: by using dict)
print("11.")
str_dict = {'num_apples': "three", 'num_peaches': "five"}
print(f"Anna has {str_dict['num_apples']} apples and {str_dict['num_peaches']} peaches.")

##################################################

# Comprehensions:
# 12. Convert (1) to list comprehension
print("12.")

# List (1) without comprehension
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print("List (1) without comprehension:\n", lst)

# List (1) with comprehension
lst_comp = [num**2 if num % 2 == 1 else num ** 4 for num in range(10)]
print("List (1) with comprehension:\n", lst_comp)

##################################################

# 13. Convert (2) to regular for with if-else
print("13.")

# List (2) with comprehension
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print("List (2) with comprehension:\n", list_comprehension)

# List (2) without comprehension
list_no_comp = []
for num in range(10):
    if num % 2 == 0:
        res = num // 2
    else:
        res = num * 10
    list_no_comp.append(res)
print("List (2) without comprehension:\n", list_no_comp)

# Note: // - floor division returns the largest integer less than or equal to the result of normal division /

##################################################

# 14. Convert (3) to dict comprehension.
print("14.")

# Dict (3) without comprehension
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print("Dict (3) without comprehension:\n", d)

# Dict (3) with comprehension
d_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print("Dict (3) with comprehension:\n", d_comp)

##################################################

# 15*. Convert (4) to dict comprehension.
print("15.")

# Dict (4) without comprehension
d4 = {}
for num in range(1, 11):
    if num % 2 == 1:
        d4[num] = num ** 2
    else:
        d4[num] = num // 0.5
print("Dict (4) without comprehension:\n", d4)

# Dict (4) with comprehension
d4_comp = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print("Dict (4) with comprehension:\n", d4_comp)

##################################################

# 16. Convert (5) to regular for with if.
print("16.")

# Dict (5) with comprehension
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print("Dict (5) with comprehension:\n", dict_comprehension)

# Dict (5) without comprehension
d5 = {}
for x in range(10):
    if x**3 % 4 == 0:
        d5[x] = x ** 3
print("Dict (4) without comprehension:\n", d5)

##################################################

# 17*. Convert (6) to regular for with if-else.
print("17.")

# Dict (6) with comprehension
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print("Dict (6) with comprehension:\n", dict_comprehension)

# Dict (6) without comprehension
dict_6_no_comp = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_6_no_comp[x] = x**3
    else:
        dict_6_no_comp[x] = x
print("Dict (6) without comprehension:\n", dict_6_no_comp)

##################################################

# Lambda:
# 18. Convert (7) to lambda function
print("18.")

# Function (7) without lambda
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print("Function (7) without lambda:\n foo(5,7)=", foo(5,7))

# Function (7) with lambda
foo_lam = lambda x, y: x if x < y else y
print("Function (7) with lambda:\n foo_lam(5,7)=", foo_lam(5,7))

##################################################

# 19*. Convert (8) to regular function
print("19.")

# Function (8) with lambda
foo = lambda x, y, z: z if y < x and x > z else y
print("Function (7) with lambda:\n foo(5,7,9)=", foo(5,7,9))

# Function (8) without lambda
def foo_no_lmb(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print("Function (7) without lambda:\n foo_no_lmb(5,7,9)=", foo_no_lmb(5,7,9))

##################################################

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print("20-24.\nlst_to_sort =",lst_to_sort)

##################################################

# 20. Sort lst_to_sort from min to max
print("20.")
# Ascending sorting using 'sorted' function
lst_sorted_A = sorted(lst_to_sort)
print("Ascending sorting using 'sorted' function:\n", lst_sorted_A)

##################################################

# 21. Sort lst_to_sort from max to min
print("21.")
# Descending sorting using 'sorted' function
lst_sorted_D = sorted(lst_to_sort, reverse=True)
print("Descending sorting using 'sorted' function:\n", lst_sorted_D)

##################################################

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print("22.")
lst_to_sort_2 = list(map(lambda x: x * 2, lst_to_sort))
print("Using map and lambda the lst_to_sort is updated by multiplying each element by 2:\n", lst_to_sort_2)

##################################################

# 23*. Raise each list number to the corresponding number on another list:
print("23.")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_raise_to_pwr = list(map(lambda x, y: x ** y, list_A, list_B))
print("Raising each list number to the corresponding number on another list:\n",
      list_A, "^", list_B, "=", lst_raise_to_pwr)

##################################################

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print("24.")
lst_to_sort_filtered = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print("Using filter and lambda to filter the odd numbers in a lst_to_sort:\n", lst_to_sort_filtered)

##################################################

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print("25.")
b = range(-10, 10)
print("From a set of values:\n", list(b), "\nusing filter function to return only negative numbers:\n",
      list(filter(lambda x: x < 0, b)))

##################################################

# 26*. Using filter function, find the values that are common to the two lists:
print("26.")
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print("Using the filter function finding common values in two lists:\n",
      list_1, "\u2229", list_2, "=", list(filter(lambda x: x in list_1, list_2)))

##################################################
#End Of Homework
##################################################
