from advent import io_utils

path = '/home/hannes/repos/advent/advent/day2/input.txt'


def is_no_letters(_id):
    return len(_id) == len(set(_id))
