from types import NoneType
from re import fullmatch


def algo_print(a):
    try:
        if a.startswith('[') and a.endswith(']'):
            a = a.lstrip('[').rstrip(']').split(',')
            d = [i.replace(' ', '') for i in a]
            a_filtered = set([int(i) for i in d if is_valid(i)])
            return a_filtered if len(a_filtered) > 0 else 'No Values'
        elif a.startswith('{') or a.startswith('('):
            return "Entered value is not valid"
        a = float(a)
        if a > 7:
            return 'Hello'
        return 'This number is not valid'
    except ValueError:
        if fullmatch(r'^[\w\s\-]+$', a):
            return ['There is no such name', 'Hello, John'][a.lower() == 'john']
        return "Entered value is not valid"
    except Exception as e:
        print(str(e))


def is_valid(x):
    try:
        if not isinstance(x, (NoneType, bool, list, dict, tuple)):
            float(x)
            return True if float(x) % 3 == 0 else False
    except ValueError:
        return False


if __name__ == "__main__":
    print('Program started, input your value(s)')
    print(algo_print(input()))
    print('Program finished')
