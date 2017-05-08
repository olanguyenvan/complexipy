import math

COMPLEXITY_LOGN = {
    'name': "logn",
    'formula': lambda size: math.log(2, size),
    'formula_for_size': lambda time, fixed_coefficient:  math.log(2, time/fixed_coefficient)
}


def solve_nlogn_equation(time, fixed_coefficient):
    min_value = 1
    max_value = 10e8
    value_looked_for = time / fixed_coefficient

    while min_value + 1 < max_value:
        middle_value = (min_value + max_value) // 2
        tmp = middle_value * math.log(2, middle_value)

        if tmp < value_looked_for:
            min_value = middle_value
        else:
            max_value = middle_value

    return min_value


COMPLEXITY_NLOGN = {
    'name': "nlogn",
    'formula': lambda size: size * math.log(2, size),
    'formula_for_size': solve_nlogn_equation,

}

COMPLEXITY_N = {
    'name': "n",
    'formula': lambda size: size,
    'formula_for_size': lambda time, fixed_coefficient: time / fixed_coefficient,
}

COMPLEXITY_N2 = {
    'name': "n^2",
    'formula': lambda size: size ** 2,
    'formula_for_size': lambda time, fixed_coefficient: math.sqrt(time / fixed_coefficient)
}


COMPLEXITY_N3 = {
    'name': "n^3",
    'formula': lambda size: size ** 3,
    'formula_for_size': lambda time, fixed_coefficient: math.pow(time / fixed_coefficient, 1/3),

}


POSSIBLE_COMPLEXITIES = [COMPLEXITY_LOGN, COMPLEXITY_NLOGN, COMPLEXITY_N, COMPLEXITY_N2, COMPLEXITY_N3]
