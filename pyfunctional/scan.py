"""
This module implements scanr and scanl
functions from functional programming.

The implementations are based on scanr and scanl
functions of the Haskell programming language.

Author : David Oniani
Date   : 04/22/2019
License: MIT
"""


from sys import setrecursionlimit
from typing import Callable, Any, Sequence
from itertools import chain


# setrecursionlimit(1_000_000)


def scanr(fun: Callable[[Any, Any], Any], acc: Any,
          trav: Sequence[Any]) -> Sequence[Any]:
    """Implementation of scanr in Python3.

    This is an implementation of the right-handed
    scan function from functional programming.

    scanr takes the second argument and the last
    item of the list and applies the function,
    then it takes the penultimate item from the
    end and the result, and so on. It returns
    the list of intermediate and final results.
    See the examples below.

    >>> print(scanr(lambda x, y: x + y, 0, [1, 2, 3]))
    [6, 5, 3, 0]
    >>> print(scanr(lambda x, y: x ** y, 0, [1, 2, 3]))
    [1, 2, 1, 0]
    """
    if not trav:
        return [acc]

    xs = scanr(fun, acc, trav[1:])
    x = xs[0]

    return list(chain([fun(trav[0], x)], xs))


def scanl(fun: Callable[[Any, Any], Any], acc: Any,
          trav: Sequence[Any]) -> Sequence[Any]:
    """Implementation of scanl in Python3.

    This is an implementation of the left-handed
    scan function from functional programming.

    scanl takes the second argument and the first
    item of the list and applies the function to
    them, then feeds the function with this result
    and the second argument and so on. It returns
    the list of intermediate and final results.
    See the examples below.

    >>> print(scanl(lambda x, y: x + y, 0, [1, 2, 3]))
    [0, 1, 3, 6]
    >>> print(scanl(lambda x, y: x ** y, 0, [1, 2, 3]))
    [0, 0, 0, 0]
    """
    if not trav:
        return [acc]

    xs = scanr(fun, acc, trav[1:])
    x = xs[0]

    return list(chain([acc], scanl(fun, fun(acc, trav[0]), trav[1:])))
