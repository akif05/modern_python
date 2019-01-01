from operator import is_not
from functools import partial

def all_subsets(n):
   
    subset = [None] * len(n)
    helper(n, subset, 0)

def helper(n, subset, i):
    if i == len(n):
        #print(*subset, sep = ", ")
        #print(*new_list, sep = ", ")
        print(*filter(None, subset), sep = ", ")
    else:
        subset[i] = None
        helper(n, subset, i+1)
        subset[i] = n[i]
        helper(n, subset, i+1)


n = {11, 22,33}
n = list(n)
all_subsets(n)
