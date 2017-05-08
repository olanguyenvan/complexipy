from complexipy.complexipy import TimeComplexity
from random import randint, choice
from string import ascii_letters


def get_strings(problem_size):
    return ''.join(choice(ascii_letters) for _ in range(problem_size))


def iterate_through_list(words):
    for _x in range(5):
        for _y in words:
            pass


def clean_after_nothing():
    pass


time_complexity_for_printing = TimeComplexity(get_strings, iterate_through_list, clean_after_nothing, 30)
complexity_for_printing = time_complexity_for_printing.get_time_complexity()
print("Complexity for printing is ", complexity_for_printing)