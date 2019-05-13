"""
This module implements the concat and concat_map
functions from functional programming.

The implementations are based on concat and concatMap
functions of the Haskell programming language.

concat accepts a sequence of sequences and concatenates them.

concat_map creates a sequence from a sequence generating function by
application of this function on all elements in a sequence passed
as the second argument.

Author : David Oniani
Date   : 04/22/2019
License: GNU General Public License v3.0
"""


from sys import setrecursionlimit
from itertools import chain
from typing import Sequence, Any, Callable
from pyfunctional.fold import foldr


setrecursionlimit(1_000_000)


def concat(seq: Sequence[Sequence[Any]]) -> Sequence[Any]:
    """Implementation of concat in Python3.

    concat accepts a sequence of sequences and concatenates them.
    See the examples below.

    >>> concat([[1, 2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> concat([["This", "is", "the"], ["concat", "function", "."]])
    ['This', 'is', 'the', 'concat', 'function', '.']
    """
    return list(foldr(lambda x, y: chain(x, y), [], seq))


def concat_map(fun: Callable[[Any], Sequence[Any]],
               seq: Sequence[Any]) -> Sequence[Any]:
    """Implementation of concat_map in Python3.

    concat_map creates a sequence from a sequence generating function by
    application of this function on all elements in a sequence passed
    as the second argument. See the examples below.

    >>> concat_map(lambda x: [x + 1], [1, 2, 3])
    [2, 3, 4]
    >>> concat_map(lambda x: [x + " "], ["a", "b", "c"])
    ['a ', 'b ', 'c ']
    """
    return list(foldr(lambda x, y: chain(fun(x), y), [], seq))
