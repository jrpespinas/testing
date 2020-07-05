from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import numpy as np


__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


def bisection_method(a, b):
    """
    A root-finding algorithm which uses an iterative method
    similar to binary search.

    Parameters
    ----------
    a : int or float
        left endpoint
    b : int or float
        right endpoint

    """
    TOL = 1e-6

    def f(x): return -10 + x * (0 + x * (4 + x))

    if f(a) * f(b) < 0:
        i = 0
        while (b - a) / 2 > TOL:
            c = (a + b) / 2

            # Check if root found or tolerance exceeded
            if f(c) == 0:
                break

            # Reassign endpoints
            if f(c) * f(a) < 0:
                b = c
            else:
                a = c

            # Tolerance
            tol = (b - a) / 2

            # Display result
            if len(sys.argv) > 1:
                print(
                    f'{i+1}:\ta={a:.6f},\tb={b:.6f},\tc={c:.6f},'
                    f'\troot={f(c):.6f}\ttolerance={tol:.6f}'
                )
            else:
                print(f'{i+1}:\t root = {c:.7f},\ttolerance = {tol:.7f}')

            i += 1
    else:
        print("Root does not exist")


if __name__ == '__main__':
    bisection_method(2, 4)

    # homework 1
    # bisection_method(0, 1)
    # bisection_method(1, 3.2)
    # bisection_method(3.2, 4)

    # homework 2
    # bisection_method(0, 1)

    # homework 3
    # bisection_method(1, 2)
    # bisection_method(2, 4)
