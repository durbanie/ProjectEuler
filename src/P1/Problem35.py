'''

Problem: The number, 197, is called a circular prime because all rotations of 
the digits: 197, 971, and 719, are themselves prime.

How many circular primes are there below one million?

Strategy: Use my prime class (which uses sets to determine if a number has 
already been determined to be prime).

Runtime: 2.3 s -> May be faster with a sieve.

Edit: Indeed it is. Down to around 300 ms.

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
    print count_circular_primes(1000000)
    StopWatch.print_time()


def count_circular_primes(N):
    '''
    Counts all circular primes up to a specified maximum.
    '''
    #_primes = set(primesfrom2to(N))
    _primes = set(sieveOfAtkin(N))
    _num = 0
    for n in _primes:
        if is_circular(n, _primes):
            _num += 1
    return _num

def is_circular(n, prime_set):
    '''
    Checks if a number is a circular prime.
    '''
    _power = int(log10(n))
    if _power == 0: return True
    _mult10 = pow(10, _power)
    _test = rotate(n, _mult10)
    while (_test != n):
        if not _test in prime_set: return False
        _test = rotate(_test, _mult10)
    return True

def rotate(n, multiple_of_10):
    '''
    Permutes a number.
    '''
    _div, _mod = divmod(n, multiple_of_10)
    return _mod * 10 + _div


if __name__ == "__main__": main()