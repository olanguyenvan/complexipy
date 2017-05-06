from random import randint
from timeout import timeout, TimeOutError
from timeit import Timer

from possible_complexities import POSSIBLE_COMPLEXITIES


class ComplexityCannotBeFound(Exception):
    pass


class ComplexityCalculator(object):
    def __init__(self, data_structure_initializer, algorithm_function, timeout=30):
        self.data_structure_initializer = data_structure_initializer
        self.algorithm_function = algorithm_function
        self.timeout = timeout
        self.quotients = {}

        for possible_complexity in POSSIBLE_COMPLEXITIES:
            self.quotients[possible_complexity['name']] = []
        self.time_complexity = None
        self.fixed_coefficient = None # for example when real complexity is multiplied by a: (a*n)

    def store_data_about_time(self, problem_size, time_decimal):
        for possible_complexity in POSSIBLE_COMPLEXITIES:
            self.quotients[possible_complexity['name']].append(time_decimal/possible_complexity['formula'](problem_size))

    @timeout()
    def calculate_time_complexity_and_coefficient(self):
        for _ in range(20):
            problem_size = randint(100000, 1000000)
            initialized_data = self.data_structure_initializer(problem_size)

            t = Timer(lambda: self.algorithm_function(initialized_data))
            time_decimal = t.timeit(number=1)

            self.store_data_about_time(problem_size, time_decimal)

        tmp_almost_accurate = ('', float('inf'))
        tmp_most_accurate = ('', float('inf'))  # store (complexity_name, complexity_coefficient)
        for complexity_name, values in self.quotients.items():
            truncated_list = sorted(values)[3:-3]
            min_value = truncated_list[0]
            max_value = truncated_list[-1]
            tmp_relative_coefficient = (max_value - min_value)/min_value

            if tmp_relative_coefficient < tmp_most_accurate[1]:
                tmp_almost_accurate = tmp_most_accurate
                tmp_most_accurate = (complexity_name, tmp_relative_coefficient)
                tmp_fixed_coefficient = (max_value - min_value) / 2

        if tmp_most_accurate[1] * 2 > tmp_almost_accurate[1]:
            raise ComplexityCannotBeFound

        self.time_complexity = next((item for item in POSSIBLE_COMPLEXITIES if item['name'] == tmp_most_accurate[0]), None)
        self.fixed_coefficient = tmp_fixed_coefficient

    def get_time_complexity(self):
        if not self.time_complexity:
            self.calculate_time_complexity_and_coefficient()
        return self.fixed_coefficient, self.time_complexity
