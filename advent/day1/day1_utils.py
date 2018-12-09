import itertools

from advent import utils


def stage_part1():
    path = '/home/hannes/repos/advent/advent/day1/input.txt'
    numbers = load_input(path)
    print(calc_part1(numbers))


def stage_part2():
    path = '/home/hannes/repos/advent/advent/day1/input.txt'
    numbers = load_input(path)
    print(calc_part2(numbers))


def calc_part1(numbers):
    return sum(numbers)


def calc_part2(numbers):
    cycle = itertools.cycle(numbers)
    cycle = itertools.chain([0], cycle)
    cycle = itertools.accumulate(cycle)
    return set_iterator(cycle)


def set_iterator(it):
    accs = set()
    for i in it:
        if i in accs:
            return i
        else:
            accs.update([i])
    return 0


def load_input(path):
    loaded = utils.load_txt(path)
    return clean_input(loaded)


def clean_input(_input):
    _input = [to_int(i) for i in _input]
    return _input


def to_int(str_num):
    return int(str_num)
