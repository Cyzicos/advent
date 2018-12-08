# -*- coding: utf-8 -*-
from advent.day2 import day2_utils


def test_no_letters():
    assert day2_utils.is_no_letters('abcdef') is True
    assert day2_utils.is_no_letters('aabcde') is False


def test_one_id():
    out = day2_utils.one_id('abcdef')
    assert not out[0]
    assert not out[1]

    out = day2_utils.one_id('abbcdef')
    assert out[0]
    assert not out[1]

    out = day2_utils.one_id('abbbcdef')
    assert not out[0]
    assert out[1]

    out = day2_utils.one_id('abbbccdef')
    assert out[0]
    assert out[1]


def test_tuple_adder():
    total = (1, 2)
    to_add = (3, 4)
    added = day2_utils.tuple_adder(total, to_add)
    assert added[0] == 4
    assert added[1] == 6


def test_do_all():
    ids = ['abbcd', 'aabcde', 'aaacde']
    twos, threes = day2_utils.do_all(ids)
    assert twos == 2
    assert threes == 1


def test_diff():
    a = 'abcde'
    b = 'abcbe'
    assert sum(day2_utils.diff(a, b)) == 1

    a = 'abcde'
    b = 'abcxy'
    assert sum(day2_utils.diff(a, b)) == 2

    a = 'abc'
    b = 'abc'
    assert sum(day2_utils.diff(a, b)) == 0


def test_iter_part2():
    ids = ['abcxy', 'abcde', 'abcbe']
    out = day2_utils.iter_part2(ids)
    assert out == 'abce'
