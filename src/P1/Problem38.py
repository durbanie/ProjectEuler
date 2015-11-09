'''

Problem: What is the largest 1 to 9 pandigital 9-digit number that can be 
    formed as the concatenated product of an integer with (1,2, ... , n) where 
    n > 1?

Strategy: Start with the largest pandigital number and check if it can be 
    deconstructed to a concatenated product.

Notes: 

Runtime: 

'''

from math import factorial

from Common.stopwatch import StopWatch


digit_power_map = [1e8, 1e7, 1e6, 1e5]
factorial_map = [factorial(x) for x in range(10)]

def find_largest_pandigital_multiple():
    '''
    Solves the problem above.
    '''
    for i in generate_pandigitals():
        if is_concatenated_product(int(i)):
            return i

def generate_pandigitals():
    '''
    Generates all 1-9 pandigital in reverse order.
    '''
    i = -1
    total = factorial_map[9]
    while i < total:
        i += 1
        digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
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


def is_concatenated_product(n):
    '''
    Checks if a pandigital number can be deconstructed to a concatenated
    product of an integer with (1, 2, ... , n) where n > 1. Returns True if it
    can, False otherwise.
    '''
    for i in range(1, 5):
        if is_concatenated_product_ndigits(n, i): return True
    return False
    
def is_concatenated_product_ndigits(p, ndigits):
    '''
    Checks for a specific concatenated product where the of an n digit integer.
    
    i - the integer
    p - the pandigital number to deconstruct
    s - the sub-pandigital number
    sstr - the sub-pandigital string
    n - the current integer in the sequence 1, 2, ...
    '''
    b, s = divmod(p, digit_power_map[ndigits - 1])
    s_str = str(int(s))
    n = 2
    while (len(s_str) != 0):
        prod = int(b * n)
        sub = str(prod)
        if not sub in s_str: return False
        if s_str.index(sub) != 0: return False
        s_str = s_str.replace(sub, "")
        n += 1
    return True

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    #print is_concatenated_product(932718654)
    print find_largest_pandigital_multiple()
    StopWatch.print_time()


if __name__ == "__main__": main()