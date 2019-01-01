
from typing import Tuple
import math

#def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
def quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
    ''' Compute the two roots of the quadratic equation:
        
        ax^2 +bx +c = 0

    Write in python:

        a*x**2 + b*x +c =0

    For example:
        >>> x1, x2 = quadratic(a=1, b=2, c=-3)
        >>> x1
        (1.0+0j)
        >>> x2
        (-3.0+0j)
        >>> 1*x1**2 + 2*x1 +(-3)
        0.0
        >>> 1*x2**2 + 2*x2 +(-3)
        0.0
    '''

    discr = math.sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discr) / (2.0*a)
    x2 = (-b - discr) / (2.0*a)

    return x1, x2

## Test the module in a go

if __name__ == '__main__':

    # This will test the code using code from For example:
    import doctest
    print(doctest.testmod())
