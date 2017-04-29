from random import randint
from timeout import timeout, TimeOutError
import math
from timeit import Timer

COMPLEXITY_NLOGN = "nlogn"
COMPLEXITY_N = "n"
COMPLEXITY_N2 = "n^2"


POSSIBLE_COMPLEXITIES = [COMPLEXITY_NLOGN, COMPLEXITY_N, COMPLEXITY_N2]


class ComplexityCannotBeFound(Exception):
    pass


class ComplexityCalculator(object):
    def __init__(self, data_structure_initializer, algorithm_function, timeout=30):
        self.data_structure_initializer = data_structure_initializer
        self.algorithm_function = algorithm_function
        self.timeout = timeout
        self.quotients = {}

        for possible_complexity in POSSIBLE_COMPLEXITIES:
            self.quotients[possible_complexity] = []
        self.time_complexity = None

    def store_data_about_time(self, problem_size, time_decimal):
        self.quotients[COMPLEXITY_N].append(time_decimal/problem_size)
        self.quotients[COMPLEXITY_N2].append(time_decimal/(problem_size*problem_size))
        self.quotients[COMPLEXITY_NLOGN].append(time_decimal/(problem_size * math.log(2, problem_size)))

    @timeout()
    def calculate_time_complexity(self):
        i = 0
        while True:
            i += 1
            problem_size = randint(100, 3000)
            initialized_data = self.data_structure_initializer(problem_size)

            t = Timer(lambda: self.algorithm_function(initialized_data))
            time_decimal = t.timeit(number=1)

            self.store_data_about_time(problem_size, time_decimal)
            if i > 20:
                break

        most_accurate = float('inf')
        found_complexity = None
        for key, values in self.quotients.items():
            truncated_list = values[3:-3]
            min_value = sorted(truncated_list)[0]
            max_value = sorted(truncated_list)[-1]
            tmp = (max_value - min_value)/min_value

            if tmp < most_accurate:
                most_accurate = tmp
                found_complexity = key

        if not found_complexity:
            raise ComplexityCannotBeFound
        self.time_complexity = found_complexity
        return self.time_complexity

    def get_time_complexity(self):
        if not self.time_complexity:
            try:
                self.calculate_time_complexity()
            except TimeOutError:
                print("timeout reached")
            except ComplexityCannotBeFound:
                raise ComplexityCannotBeFound

        return self.time_complexity
