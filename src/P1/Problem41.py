'''

Problem: We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

Strategy: Brute force

Notes: 

Runtime: 

'''

from math import factorial

from Common.stopwatch import StopWatch
from Common.primetester import PrimeTester

factorial_map = [factorial(x) for x in range(10)]

def check_largest_pandigital_prime(max_digits_to_check):
    tester = PrimeTester()
    for nmax in [7, 4, 1]:
        if nmax > max_digits_to_check: continue
        for n in generate_pandigitals(nmax):
            if tester.is_prime(int(n)):
                return n
    return 0

def generate_pandigitals(n):
    '''
    Generates all 1-9 pandigital in reverse order.
    '''
    i = -1
    total = factorial_map[n] - 1
    while i < total:
        i += 1
        digits = [str(j) for j in range(n, 0, -1)]
        yield generate_kth_permutation(i, digits)

def generate_kth_permutation(k, digits):
    '''
    Generates the kth permutation of the given digits.
    '''
    _final = ""
    while len(digits) > 0:
        _digit, k = get_spot(k, digits)
        _final = _final + _digit
    return _final

def get_spot(n, digits):
    '''
    Gets the next digit for the nth permutation of the (remaining) digits.
    '''
    _N = len(digits) - 1
    _Nfac = factorial_map[_N]
    _index = n / _Nfac
    _remaining = n % _Nfac
    
    if (_index >= len(digits)):
        print "Index out of range!"
        digits = []
        return '', 0
    
    _digit = digits.pop(_index)
    return _digit, _remaining


def main():
    '''
    Main entry point.
    '''
    
    StopWatch.start()
    print check_largest_pandigital_prime(9)
    StopWatch.print_time()


if __name__ == "__main__": main()