"""
Testing module

David Oniani
Licensed under MIT
"""


import pytest

from pyfunctional.fold import foldr, foldl
from pyfunctional.concat import concat, concat_map
from pyfunctional.scan import scanr, scanl


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


def test_scan():
    """Testing scan module"""
    xs = [0, 52_378]
    ys = [17, 45, 917]
    zs = [21, 52, 125, 390]
    ts = [124, 19, -512, 76, 742]

    assert scanr(lambda x, y: x + y, 0, xs) == [52_378, 52_378, 0]
    assert scanr(lambda x, y: x - y, 0, ys) == [889, -872, 917, 0]
    assert scanr(lambda x, y: x - y, 1, zs) == [-295, 316, -264, 389, 1]
    assert scanr(lambda x, _: x, 3, ts) == [124, 19, -512, 76, 742, 3]

    assert scanl(lambda x, y: x + y, 0, xs) == [0, 0, 52_378]
    assert scanl(lambda x, y: x - y, 0, ys) == [0, -17, -62, -979]
    assert scanl(lambda x, y: x - y, 1, zs) == [1, -20, -72, -197, -587]
    assert scanl(lambda x, _: x, 3, ts) == [3, 3, 3, 3, 3, 3]
