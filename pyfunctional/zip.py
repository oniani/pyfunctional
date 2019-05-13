"""
This module implements zip_with
function from functional programming.

The implementations are based on zipWith
function of the Haskell programming language.

Author : David Oniani
Date   : 04/23/2019
License: GNU General Public License v3.0
"""


from sys import setrecursionlimit
from typing import Callable, Sequence, Any
from itertools import chain


setrecursionlimit(1_000_000)


def zip_with(fun: Callable[[Any, Any], Any], xs: Sequence[Any],
             ys: Sequence[Any]) -> Sequence[Any]:
    """Implementation of zip_with in Python3.

    This is an implementation of the zip_with
    function from functional programming.

    zip_with makes a list, its elements are
    calculated from the function and the elements
    of input lists occuring at the same position
    in both lists. See examples below.

    >>> foldr((lambda _, y: y + 1), 0, [0, 1, 2, 3, 4])
    5
    >>> foldr((lambda x, y: x + y), 0, [0, 1, 2, 3, 4])
    10


    """
    if not xs:
        return []

    return [fun(xs[0], ys[0])] + zip_with(fun, xs[1:], ys[1:])
