from calculate_complexity import ComplexityCalculator, ComplexityCannotBeFound
from timeout import TimeOutError


class TimeComplexity(object):
    def __init__(self, data_structure_initializer, algorithm_function, clean_up_code_function, timeout=30):
        self.timeout = timeout
        self.data_structure_initializer = data_structure_initializer
        self.algorithm_function = algorithm_function
        self.clean_up_code_function = clean_up_code_function
        self.time_complexity = None
        self.fixed_coefficient = None

    def get_time_complexity(self):
        if not self.time_complexity:
            complexity_calculator = ComplexityCalculator(self.data_structure_initializer,
                                                         self.algorithm_function, self.timeout)
            try:
                self.fixed_coefficient, self.time_complexity = complexity_calculator.get_time_complexity()
            except TimeOutError:
                print("Timeout has been to small to find out what the complexity is.")
                return
            except ComplexityCannotBeFound:
                print("Complexity cannot be found!")
                return
        return self.time_complexity['name']

    def get_probable_time_per_problem_size(self, problem_size):
        if not self.fixed_coefficient:
            self.get_time_complexity()
        return self.fixed_coefficient * self.time_complexity['formula'](problem_size)

    def get_max_problem_size_per_time(self, time):
        if not self.fixed_coefficient:
            self.get_time_complexity()
        return self.time_complexity['formula_for_size'](time, self.fixed_coefficient)
