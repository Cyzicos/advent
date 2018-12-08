

path = '/home/hannes/repos/advent/day1/input.txt'


def load_input(path):
    loaded = load_txt(path)
    return clean_input(loaded)


def load_txt(path):
    with open(path) as f:
        content = f.readlines()
    return content


def clean_input(_input):
    _input = [i.strip() for i in _input]
    _input = [to_int(i) for i in _input]
    return _input


def to_int(str_num):
    return int(str_num)


def calc_part1(numbers):
    return sum(numbers)
