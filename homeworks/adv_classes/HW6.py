######################################
# HW#6 'Classes lecture 2' Ivan Diulin
######################################

import dataclasses  # importing libraries for task 6
from collections import namedtuple  # importing libraries for task 7

#########################
# 1. Making classes Laptop and Battery with composition


class Battery:
    def __init__(self, num, capacity: int):
        self.num = num
        self.capacity = capacity


class Laptop:
    def __init__(self, num_bat):
        self.num_bat = num_bat
        self.battery = []
        self.total_capacity = 0

        for num in range(num_bat):
            # setting number and same capacity for every Battery-type object in created list
            self.battery.append(Battery(num, 3000))
            # calculating total capacity of Laptop's battery pack
            self.total_capacity += self.battery[num].capacity


laptop_1 = Laptop(10)
print(f"1.\nLaptop has {laptop_1.num_bat} batteries"
      f" with total capacity of {laptop_1.total_capacity} mAh.")


#########################
# 2. Making classes Guitar and GuitarString with aggregation

class GuitarString:
    pass


class Guitar:
    def __init__(self, guitar_string: GuitarString):
        self.guitar_string = guitar_string


g_str_1 = GuitarString()
guitar_1 = Guitar(g_str_1)


#########################
# 3. Creating class Calc with static method for addition of 3 parameters

class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


num_1 = 1
num_2 = 4
num_3 = 10
print(f"3.\nCalling static method from class itself without object creation for adding three numbers:\n"
      f" {num_1} + {num_2} + {num_3} = {Calc.add_nums(num_1, num_2, num_3)}.")


#########################
# 4*. Making class Pasta with different sets of ingredients

class Pasta:
    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    # adding class method 'carbonara' which takes class Pasta as 'cls' parameter
    # and returns it to the program while defining in brackets its attribute
    # 'ingredients' by assigning to it the list with desired values of pasta ingredients

    @classmethod
    def carbonara(cls):
        ingredients = ['forcemeat', 'tomatoes']
        return cls(ingredients)

    # same as above method for different recipe

    @classmethod
    def bolognaise(cls):
        return cls(ingredients=['bacon', 'parmesan', 'eggs'])


print("4.\nCreating objects of class Pasta with different sets of ingredients:")

pasta_1 = Pasta(["tomato", "cucumber"])
print("The user-defined ingredients of pasta_1 object:\n", pasta_1.ingredients)

pasta_2 = Pasta.carbonara()
print("The pre-defined ingredients of carbonara recipe"
      " for pasta_2 object:\n", pasta_2.ingredients)

pasta_3 = Pasta.bolognaise()
print("The pre-defined ingredients of bolognaise recipe"
      " for pasta_3 object:\n", pasta_3.ingredients)

#########################
# 5*. Making class Concert with check of value of visitors_count attribute


class Concert:
    max_visitor_num = 50

    def __init__(self, visitors_count):
        self.visitors_count = visitors_count
        if self.visitors_count > self.max_visitor_num:
            self.visitors_count = self.max_visitor_num


print("5.\nCreating objects of class Concert with with check of attribute visitors_count:")

concert_1 = Concert(35)
print("With concert_1 = Concert(35), concert_1.visitors_count=", concert_1.visitors_count)

concert_2 = Concert(10000)
print("With concert_2 = Concert(10000), concert_2.visitors_count=", concert_2.visitors_count)

concert_3 = Concert(50)
print("With concert_3 = Concert(50), concert_3.visitors_count=", concert_3.visitors_count)


#########################
# 6. Creating dataclass AddressBookDataClass with 7 fields

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


person_1 = AddressBookDataClass(1, "John Stewart", "+10987654321",
                                "2800 Pennsylvania Avenue Northwest Washington, D.C., US",
                                "john.stewart.email@yahoo.com", "25.01.1975", 47)
print(f"6.\nPrinting person's data from object of dataclass type:\n"
      f" Database 'key' field: {person_1.key}"
      f" Hi, my name is {person_1.name}, you can call me at {person_1.phone_number}\n"
      f" or send me a letter to {person_1.address},\n"
      f" or e-mail me at {person_1.email}.\n"
      f" I was born on {person_1.birthday} thus I am {person_1.age} years old now.")

print("person_1 = ", person_1)

#########################
# 7.1. Creating class with the same attributes as in 6 task but with NamedTuple


# function for printing named tuple with its field names
def print_tuple(n_tuple):
    for i in range(len(n_tuple)):
        print(f" {n_tuple._fields[i]} = {n_tuple[i]}")


AddressBookNamedTuple = namedtuple("AddressBookNamedTuple", ("key", "name", "phone_number",
                                                             "address", "email", "birthday", "age"))
address_book = AddressBookNamedTuple(2, "Fill Pitkins", "+443332355505",
                                     "12 Kingston Rd, Tolworth, Chessington, Surbiton KT5 9NU, GB",
                                     "fill.pitkins.email@proton.me", "15.02.1980", 42)

print(f"7.1.\nPrinting person's data from named tuple object 'address_book':")
print_tuple(address_book)


# 7.2. Creating the same class as in task 7.1. but with data taken from dict and tuple
data_fields_dict = {"AddressBookNamedTuple1": ("key", "name", "phone_number", "address",
                                               "email", "birthday", "age")}
data_set_tuple = (3, "Samantha Pitkins", "+443332377707",
                  "374 Seven Sisters Rd, Finsbury Park, London N4 2PG",
                  "sam.pitkins.the.best@proton.me", "18.08.1980", 41)

AddressBookNamedTuple1 = namedtuple("AddressBookNamedTuple1", data_fields_dict["AddressBookNamedTuple1"])
address_book_1 = AddressBookNamedTuple1(*data_set_tuple)

print(f"7.2.\nPrinting named tuple 'address_book_1', created from dict and tuple:")
print_tuple(address_book_1)

print("Named tuple from 'address_book_1' representation without unpacking:\n", address_book_1)


#########################
# 8. Creating regular class AddressBook with 7 parameters from task 6 and forcing
# its str() representation to be the same as for data class AddressBookDataClass from task 6

class AddressBook:
    def __init__(self, key: int, name: str, phone_number: str,
                 address: str, email: str, birthday: str, age: int):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{AddressBook.__name__}(key='{self.key}', name='{self.name}',"\
               f" phone_number='{self.phone_number}', address='{self.address}',"\
               f" email='{self.email}', birthday= '{self.birthday}', age='{self.age}')"


address_book_2 = AddressBook(4, "Agatha Kelly", "+16477654321",
                             "550 Wellington St W, Toronto, ON, M5V2V4, Canada",
                             "agatha.kelly.artdealer@proton.me", "18.08.1990", 31)

print(f"8.\nObject of regular class AddressBook with changed str() representation:\n"
      f"{str(address_book_2)}")


#########################
# 9. Changing the value of the age property of the Person object using setattr()

class Person:
    name = "John"
    age = 36
    country = "USA"


john = Person()

print("9.\nChanging value of the age property of the Person object:")
print(f"  Creating {john.name} object with attributes:\n"
      f"    Name = {john.name}, age = {john.age}, country = {john.country}.")

setattr(john, 'age', 29)

print(f"  Changing value of the age property of {john.name} object:")
print(f"    Name = {john.name}, age = {john.age}, country = {john.country}.")


#########################
# 10. Adding attributes to instance of Student class

class Student:

    def __init__(self, id_: int, name: str):
        self.id_ = id_
        self.name = name


student = Student(0, "Orest")
student.email = "orest12@gmail.com"
setattr(student, "email", "new.orest12@gmail.com")
print(f"10.\n Student's data:\nid = {student.id_}, name = {student.name}, email = {student.email}")

student_email = getattr(student, "email")
print(f" New variable student_email = {student_email}")


#########################
# 11*. By using @property converting the celsius to fahrenheit

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


t = 25
fahrenheit = Celsius(t)
print(f"11.\nConverting Celsius to Fahrenheit: {t}\u00BAC = {fahrenheit.temperature}\u00BAF")
