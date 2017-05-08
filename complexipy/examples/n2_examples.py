from complexipy.complexipy import TimeComplexity
from random import randint


def clean_after_nothing():
    pass


def generate_list(problem_size):
    l = [randint(10, 100) for _ in range(problem_size)]
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

