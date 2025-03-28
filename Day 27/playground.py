from functools import total_ordering


def add(*args):
    total = 0
    for n in args:
        total += n
    return total

value = add(10,20,20)

print(value)
