'''

Problem: Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left.

Strategy: Brute force, similar to circular prime strategy.

Notes: No idea what the theoritical limit is, or why we can know that there are
only 11. For the purposes of this problem, I will take the hint that there are
only 11 and stop the search once 11 is found. Since we don't know what the 
theoretical limit is, and since my strategy requires the creation of a set of
primes up to some number, I will start with some max (e.g. 10), see if there
are 11, and if not, try 10 * the previous number, recursively until the 11 are
found. This should not increase the run time significantly, since the additional
run time of the previous function calls will be ~ 1/10 the final.

Runtime: 269 ms

'''

from math import log10
from math import pow

from Common.primesieve import sieveOfAtkin
from Common.stopwatch import StopWatch

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    print sum_truncatable_primes(10)
    StopWatch.print_time()


def sum_truncatable_primes(N):
    '''
    Counts all truncatable.
    '''
    #print "Trying", N
    _primes = set(sieveOfAtkin(N))
    _num, _sum = 0, 0
    for n in _primes:
        if n / 10 == 0: continue
        if _num == 11: break
        if is_truncatable(n, _primes):
            _num += 1
            _sum += n
            #print "  ", _num, ":", n
    if _num < 11:
        return sum_truncatable_primes(N*10)
    return _num, _sum

def is_truncatable(n, prime_set):
    '''
    Checks if a number is a circular prime.
    '''
    
    _left = truncate_left(n)
    while _left > 0:
        if not _left in prime_set:
            return False
        _left = truncate_left(_left)
    
    _right = truncate_right(n)
    while _right > 0:
        if not _right in prime_set:
            return False
        _right = truncate_right(_right)

    return True

def truncate_left(n):
    '''
    Truncates left, e.g. 3797 -> 797
    '''
    return int(n % (pow(10, int(log10(n)))))

def truncate_right(n):
    '''
    Truncates right, e.g. 3797 -> 379
    '''
    return n // 10


if __name__ == "__main__": main()