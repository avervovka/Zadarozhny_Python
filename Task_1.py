from types import NoneType
import re


def algo_print(a):
    print(a, type(a))
    try:
        if a.startswith('[') and a.endswith(']'):
            a = list(a)
            a_filtered = [i for i in a if is_valid(i)]
            return a_filtered
        elif a.startswith('{') or a.startswith('('):
            return "Entered value is not valid"

        a = float(a)
        if a > 7:
            return 'Hello'
        return 'This number is not valid'
    except ValueError:
        if re.fullmatch('[a-zA-Z]', a):
            return ['There is no such name', 'Hello, John'][a.lower() == 'john']
        return 'Not Valid'
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
    print('Program Started')
    print(algo_print(input()))
    print('Program Finished')
