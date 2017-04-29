from calculate_complexity import ComplexityCalculator


class TimeComplexity(object):
    def __init__(self, data_structure_initializer, algorithm_function, clean_up_code_function, timeout=30):
        self.timeout = timeout
        self.data_structure_initializer = data_structure_initializer
        self.algorithm_function = algorithm_function
        self.clean_up_code_function = clean_up_code_function
        self.time_complexity = None

    def get_time_complexity(self):
        if not self.time_complexity:
            complexity_calculator = ComplexityCalculator(self.data_structure_initializer,
                                                         self.algorithm_function, self.timeout)
            self.time_complexity = complexity_calculator.get_time_complexity()

        return self.time_complexity

    def get_probable_time_per_problem_size(self):
        pass

    def get_max_problem_size_per_time(self):
        pass
