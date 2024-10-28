from array import *


def algo_print(a):
    if isinstance(a, int):
        if a > 7:
            return 'Hello'
    elif isinstance(a, str):
        return ['There is no such name', 'Hello, John'][a == 'John']
    elif isinstance(a, array):
        a_filtered = list(filter(lambda x: x % 3 == 0, a))
        return a_filtered
