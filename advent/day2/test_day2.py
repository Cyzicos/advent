# -*- coding: utf-8 -*-
from advent.day2 import day2_utils


def check_no_letters():
    assert day2_utils.is_no_letters('abcdef') is True
    assert day2_utils.is_no_letters('aabcde') is False
