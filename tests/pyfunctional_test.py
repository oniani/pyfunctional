"""
Testing module

David Oniani
Licensed under MIT
"""


import pytest

from pyfunctional.fold import foldr, foldl
from pyfunctional.concat import concat, concat_map


def test_fold():
    """Testing fold module"""
    xs = list(range(10_000))
    ys = list(range(10_000))

    assert foldr(lambda x, y: x + y, 0, xs) == sum(xs)
    assert foldr(lambda x, y: x + y, 0, ys) == sum(ys)
    assert foldr(lambda _, y: y + 1, 0, xs) == len(xs)
    assert foldr(lambda _, y: y + 1, 0, ys) == len(ys)

    assert foldl(lambda x, y: x + y, 0, xs) == sum(xs)
    assert foldl(lambda x, y: x + y, 0, ys) == sum(ys)
    assert foldl(lambda x, _: x + 1, 0, xs) == len(xs)
    assert foldl(lambda x, _: x + 1, 0, ys) == len(ys)


def test_concat():
    """Testing concat module"""
    xss = [list(range(10)) for _ in range(1_000)]
    ys = list(range(10_000))

    assert concat(xss) == 1_000 * list(range(10))
    assert concat_map(lambda x: [x**2], ys) == [i**2 for i in range(10_000)]
