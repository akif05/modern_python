
from quadratic import quadratic
import py.test
import itertools
from hypothesis import given, assume, strategies as st
import cmath

# it used to test the quadratic function
# py.test test_qudratic.py 
def test_quadratic():
    x1, x2 = quadratic(a=1, b=2, c=-3)
    assert 1*x1**2 + 2*x1 +(-3) == 0
    assert 1*x2**2 + 2*x2 +(-3) == 0

def test_quadratic_types():
    with py.test.raises(TypeError):
        quadratic(a=1, b="hh", c=-3)
    with py.test.raises(TypeError):
        quadratic(a=1, b=2, c=-3, d=4)

#def test_torture_test():
    args = [10, 0, 1, 18, -5, -1, 0.5, -1.5]
    # In for each time get on combination of tree numbers from args
    # And use thise number in quadratic function
    for a, b, c in itertools.permutations(args, 3):
        if a == 0:
            with py.test.raises(ZeroDivisionError):
                quadratic(a, b, c)
        else:
            x1, x2 = quadratic(a, b, c)
            assert cmath.isclose(a*x1**2 + b*x1 + c == 0, 0.0, abs_tol=0.0001)

# a = 0.0010000000000002, b = 23384.003335789970
# c = 0.0010000000000002
@given(
    st.floats(min_value=-1000, max_value=1000),
    st.floats(min_value=-1000, max_value=1000),
    st.floats(min_value=-1000, max_value=1000),
)
def test_qudratic_hypo(a, b, c):
    # will stop generating a less than 0.001 ~~ 0 to avoid devision by 0   /2a
    assume(abs(a) > 0.001)
    assume(abs(b) > 0.001)
    assume(abs(c) > 0.001)
    x1, x2 = quadratic(a, b, c)
    assert cmath.isclose(a*x1**2 + b*x1 + c == 0, 0.0, abs_tol=0.0001)
    assert cmath.isclose(a*x2**2 + b*x2 + c == 0, 0.0, abs_tol=0.0001)
