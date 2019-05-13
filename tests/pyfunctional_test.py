"""
Testing module

David Oniani
Licensed under GNU General Public License v3.0
"""


import pytest

from pyfunctional.fold import foldr, foldl
from pyfunctional.concat import concat, concat_map
from pyfunctional.scan import scanr, scanl
from pyfunctional.zip import zip_with
from pyfunctional.all_any import all, any


def test_fold():
    """Testing fold module."""
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
    """Testing concat module."""
    xss = [list(range(10)) for _ in range(1_000)]
    ys = list(range(10_000))

    assert concat(xss) == 1_000 * list(range(10))
    assert concat_map(lambda x: [x**2], ys) == [i**2 for i in range(10_000)]


def test_scan():
    """Testing scan module."""
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


def test_zip():
    """Testing zip module."""
    xs = [612, 46, -52]
    ys = [151, 412, 812]
    zs = [829, 135, -149, 436, 25]
    ts = [35, -135, 464, 76, 13]

    assert zip_with(lambda x, y: x + y, xs, ys) == [763, 458, 760]
    assert zip_with(lambda x, y: x * y, xs, ys) == [92_412, 18_952, -42_224]
    assert zip_with(lambda x, y: x - y, zs, ts) == [794, 270, -613, 360, 12]
    assert zip_with(lambda _, y: y, zs, ts) == [35, -135, 464, 76, 13]


def test_all_any():
    """Testing all_any module."""
    xs = [1, 2, 3]
    ys = [1, 3, 5]
    zs = [1, 2, 3, 4]
    ts = [2, 4, 6, 8]

    assert all(lambda x: x % 2 == 0, xs) is False
    assert all(lambda x: x % 2 == 1, ys) is True
    assert all(lambda x: x % 2 == 1, zs) is False
    assert all(lambda x: x % 2 == 0, ts) is True

    assert any(lambda x: x % 2 == 0, xs) is True
    assert any(lambda x: x % 2 == 0, ys) is False
    assert any(lambda x: x % 2 == 1, zs) is True
    assert any(lambda x: x % 2 == 1, ts) is False
