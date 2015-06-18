'''

Problem: Consider all numbers generated from

a^b where 2 <= a, b <= 100

How many distinct terms are there?

Strategy: Some mathematical analysis, data-structures

Notes: Brute force is possible with python. It will happily calculate integer
powers up to 100^100. I want this algorithm to be guaranteed to work on other 
languages (for example, using floats would probably work, but it may not be 
guaranteed).

Any number can be decomposed into a distinct list of prime divisors. For
example, the number 12 = 2*2*3. Since 12 cannot be decomposed into any other set
of primes, we can count the number of prime patterns that we see. So for 12^3,
we get (2*2*3) = 2*2*2*2*2*2*3*3*3. We repeat this for all possible numbers 
(approximately 100*100 possibilities in this case) and store them in a set. The
number of entries in the set will be equal to the number of distinct terms.
 
'''

import sets

from Common.stopwatch import StopWatch
from Common.prime import Prime

primes = Prime().get_primes(100)

def decompose(N):
    '''Decomposes the input N into a unique list of primes'''
    _decomp = []
    for n in primes:
        _div, _mod = divmod(N, n)
        while (_mod == 0):
            _decomp.append(n)
            N = N / n
            _div, _mod = divmod(N, n)
        if N == 1: break
    return _decomp

def stringify(decomp):
    '''Converts the list [X, Y, ...] to a string of the form X*Y*...'''
    return "*".join(str(n) for n in decomp)

def determine_unique(amax, bmax):
    '''Determines the number of unique powers'''
    _set = sets.Set([])
    for a in range(2, amax):
        _decomp = decompose(a)
        for b in range(2, bmax):
            _decomp_pow = _decomp * b
            _decomp_pow.sort()
            #print stringify(_decomp_pow)
            _set.add(stringify(_decomp_pow))
    return len(_set)            

def main():
    StopWatch.start()
    print determine_unique(101, 101)
    StopWatch.print_time()
    
if __name__ == '__main__':
    main()