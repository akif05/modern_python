
from typing import *
from collections import OrderedDict, deque,namedtuple

x = 10  # type: int 

def f(x: int,y: int) -> int:
    return(x+y)

print(f(10, 20))
y = OrderedDict()  # type: OrderedDict

def g(x: List[int]) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

g([10, 20, 30])

hts = [97.1, 111.2]                 # type: List[float]
person = ('Raymond', 5*12 + 11)     #Tuple[str, float

info = ('Pearson', 'Course', 'Python')  # type: Tuple[str, ...]

fifo = deque()          # type: deque
Point = NamedTuple('Point', [('x', int), ('y', int)])
print(Point)

# python -m mypy typeedit.py 
# python -m pyflakes typeedit.py 
# hypothesis
# unittesta -> nose test.py 


#from typing import *
#from collections import OrderedDict
#
#x = 10  # type: int 
#
#def f(x: int,y: int) -> int:
#    return(x+y)
#
#print(f(10, 20))
#y = OrderedDict()  # type: OrderedDict
#
#def g(x: Sequence):
#    print(len(x))
#    print(x[2])
#    for i in x:
#        print(i)
#    print()
#
#g([10, 20, 30])
#g('abcdef')
#g((11,12,13))
##g([None])



#from typing import *
#
#x = 10  # type: int 
#
#def f(x,y):
#    return(x+y)
#
#print(f(10, 20))
#
#print(f('hello ', 'world'))
#print(f('hello ', '))
