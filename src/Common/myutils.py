'''
Common utility functions. If they're used more 
than once in Project Euler, they should go here.
'''

import math

def divisors(n):
    '''
    Returns a list of all divisors of n.
    '''
    if n < 2:
        return [0]
    _divs = [1]
    _rootn = int(math.sqrt(n))
    for x in range(2, _rootn+1):
        _div = divmod(n, x)
        if _div[1] == 0:
            _divs.append(x)
            if x != _div[0]:
                _divs.append(_div[0])
    return _divs

def generate_range(start, end):
    '''
    Experimenting with python generation.
    '''
    index = start
    while (index < end):
        yield index
        index += 1