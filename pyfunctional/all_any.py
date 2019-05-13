"""
This module implements all and an
functions from functional programming.

The implementations are based on all and any
functions of the Haskell programming language.

Author : David Oniani
Date   : 04/23/2019
License: GNU General Public License v3.0
"""


from sys import setrecursionlimit
from typing import Callable, Sequence, Any
from pyfunctional.fold import foldr


setrecursionlimit(1_000_000)


def all(fun: Callable[[Any], bool], seq: Sequence[Any]) -> bool:
    """Implementation of all in Python3.

    This is an implementation of any function
    from functional programming. See examples
    below.

    >>> foldl((lambda x, _: x + 1), 0, [0, 1, 2, 3, 4])
    5
    >>> foldl((lambda x, y: x + y), 0, [0, 1, 2, 3, 4])
    10
    """
    return foldr((lambda x, y: x and y), True, list(map(fun, seq)))


def any(fun: Callable[[Any], bool], seq: Sequence[Any]) -> bool:
    """Implementation of any in Python3.

    This is an implementation of any function
    from functional programming. See examples
    below.

    >>> foldl((lambda x, _: x + 1), 0, [0, 1, 2, 3, 4])
    5
    >>> foldl((lambda x, y: x + y), 0, [0, 1, 2, 3, 4])
    10
    """
    return foldr((lambda x, y: x or y), False, list(map(fun, seq)))
