'''

Problem:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

Solution: Brute-force

Notes: Not many calculations to do, so I'm more worried about organization of
the calculations than I am with their efficiency.

Run-time: 9 ms

'''

from Common.stopwatch import StopWatch
from Common.primesieve import sieveOfAtkin

primes = sieveOfAtkin(9802)

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    _list = listDigitCancellingFractions()
    _num, _den = 1, 1
    print _list
    for _tuple in _list:
        _num *= _tuple[0]
        _den *= _tuple[1]
    print lowestCommonTerms(_num, _den)
    StopWatch.print_time()


def listDigitCancellingFractions():
    '''
    Lists all fractions which are equal to their digit cancelling values.
    '''
    _dcvs = []
    for i in range(10, 99):
        for j in range(i+1, 99):
            _dcv = digitCancellingValue(i, j)
            if equalFractions(i, j, _dcv[0], _dcv[1]):
                _dcvs.append(_dcv)
    return _dcvs
    
def equalFractions(num1, den1, num2, den2):
    '''
    Determines if two fractions are equal (to avoid potential rounding errors).
    '''
    if num2 <= 0 or den2 <= 0: return False
    _frac1 = lowestCommonTerms(num1, den1)
    _frac2 = lowestCommonTerms(num2, den2)
    return _frac1 == _frac2        

def lowestCommonTerms(num, den):
    '''
    Given a numerator and denominator, re-expresses it in it's lowest common
    terms.
    '''
    _num, _den = num, den
    for i in primes:
        if i > _num: break
        while _num % i == 0 and _den % i == 0:
            _num //= i
            _den //= i
    return _num, _den

def digitCancellingValue(num, den):
    '''
    Finds if there is a "digit cancelling value" and returns the numerator and
    denominator. If there isn't a digit cancelling possibility, returns 0, 0 or
    -1, -1.
    '''
    _num1 = num % 10
    _num10 = num // 10
    _den1 = den % 10
    _den10 = den // 10
    if (_num1 == 0 or _num10 == 0): return 0, 0
    if (_den1 == 0 or _den10 == 0): return 0, 0
    if (_num1 == _den1): return _num10, _den10
    if (_num10 == _den1): return _num1, _den10
    if (_num1 == _den10): return _num10, _den1
    if (_num10 == _den10): return _num1, _den1
    return -1, -1

if __name__ == '__main__':
    main()