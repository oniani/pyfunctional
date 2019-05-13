"""
This module implements foldr and foldl
functions from functional programming.

The implementations are based on foldr and foldl
functions of the Haskell programming language.

Author : David Oniani
Date   : 04/22/2019
License: GNU General Public License v3.0
"""


from sys import setrecursionlimit
from typing import Callable, Sequence, Any


setrecursionlimit(1_000_000)


def foldr(fun: Callable[[Any, Any], Any], acc: Any, seq: Sequence[Any]) -> Any:
    """Implementation of foldr in Python3.

    This is an implementation of the right-handed
    fold function from functional programming.

    If the list is empty, we return the accumulator
    value. Otherwise, we recurse by applying the
    function which was passed to the foldr to
    the head of the iterable collection
    and the foldr called with fun, acc, and
    the tail of the iterable collection.

    Below are the implementations of the len
    and sum functions using foldr to
    demonstrate how foldr function works.

    >>> foldr((lambda _, y: y + 1), 0, [0, 1, 2, 3, 4])
    5
    >>> foldr((lambda x, y: x + y), 0, [0, 1, 2, 3, 4])
    10

    foldr takes the second argument and the
    last item of the list and applies the function,
    then it takes the penultimate item from the end
    and the result, and so on.
    """
    return acc if not seq else fun(seq[0], foldr(fun, acc, seq[1:]))


def foldl(fun: Callable[[Any, Any], Any], acc: Any, seq: Sequence[Any]) -> Any:
    """Implementation of foldl in Python3.

    This is an implementation of the left-handed
    fold function from functional programming.

    If the list is empty, we return the accumulator
    value. Otherwise, we recurse with a new accumulator
    value which is a result of the function application
    on the old accumulator value and the head of the list.

    Below are the implementations of the len
    and sum functions using foldl to
    demonstrate how foldl function works.

    >>> foldl((lambda x, _: x + 1), 0, [0, 1, 2, 3, 4])
    5
    >>> foldl((lambda x, y: x + y), 0, [0, 1, 2, 3, 4])
    10

    foldl takes the second argument and the
    first item of the list and applies the function
    to them, then feeds the function with this result
    and the second argument and so on.
    """
    return acc if not seq else foldl(fun, fun(acc, seq[0]), seq[1:])
