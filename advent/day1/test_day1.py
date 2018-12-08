# -*- coding: utf-8 -*-
from advent.day1 import day1_utils


def test_load():
    path = 'input.txt'
    assert day1_utils.load_input(path)[0] == 19


def test_to_int():
    assert isinstance(day1_utils.to_int('+19'), int)


def test_to_int_edge():
    assert day1_utils.to_int('+19') == 19
    assert day1_utils.to_int('-19') == -19


def test_part1():
    assert day1_utils.calc_part1([1, 2, 3]) == 6


def test_part2():
    assert day1_utils.calc_part2([1, 2, 3]) == 0
    assert day1_utils.calc_part2([1, 2, 3, -5]) == 1
    assert day1_utils.calc_part2([1, -1]) == 0


def test_set_iterator():
    assert day1_utils.set_iterator([1, 2, 3]) == 0
    assert day1_utils.set_iterator([1, 3, 1, -5]) == 1
