from complexipy import TimeComplexity
from random import randint, choice
from string import ascii_letters


def get_strings(problem_size):
    return ''.join(choice(ascii_letters) for _ in range(problem_size))


def print_strings(words):
    for _ in words:
        pass
    for _ in words:
        pass
    for _ in words:
        pass


def clean_after_nothing():
    pass


time_complexity_for_printing = TimeComplexity(get_strings, print_strings, clean_after_nothing, 30)
complexity_for_printing = time_complexity_for_printing.get_time_complexity()
print("Complexity for printing is ", complexity_for_printing)


def generate_list(problem_size):
    l = [randint(10000, 11000) for _ in range(problem_size)]
    return l


def bubble_sort(list_to_sort):
    for passnum in range(len(list_to_sort)-1, 0, -1):
        for i in range(passnum):
            if list_to_sort[i] > list_to_sort[i+1]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i+1]
                list_to_sort[i+1] = temp


time_complexity_for_bubble_sort = TimeComplexity(generate_list, bubble_sort, clean_after_nothing, 300)
complexity_for_bubble_sort = time_complexity_for_bubble_sort.get_time_complexity()
print("Complexity for bubble sort is ", complexity_for_bubble_sort)


time_complexity_for_merge_sort = TimeComplexity(generate_list, sorted, clean_after_nothing, 30)
complexity_for_merge_sort = time_complexity_for_merge_sort.get_time_complexity()
print("Complexity for python `sorted`is ", complexity_for_merge_sort)
