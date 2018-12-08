import collections
import itertools

from advent import io_utils


def is_no_letters(_id):
    return len(_id) == len(set(_id))


def do_all(ids):
    out = (one_id(_id) for _id in ids)
    acc = itertools.accumulate(out, func=tuple_adder)
    return collections.deque(acc, maxlen=1).pop()


def one_id(_id):
    counter = collections.Counter(_id)
    two = 2 in counter.values()
    three = 3 in counter.values()
    return two, three


def tuple_adder(total, elem):
    return total[0]+elem[0], total[1]+elem[1]


def stage_part1():
    path = '/home/hannes/repos/advent/advent/day2/input.txt'
    ids = io_utils.load_txt(path)
    twos, threes = do_all(ids)
    return twos*threes
