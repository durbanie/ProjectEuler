'''

Problem: We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

Stragegy: Brute-force, with some restraints on numbers to try.

Notes: Tried this two ways, one using strings and another finding the list of
digits. Turns out the conversion to strings is at least 2x faster.
'''

from Common.stopwatch import StopWatch


##############################################################################
# Using digits
def is_1_9_pandigital_group(n1, n2, n3):
    '''
    Checks if 3 numbers are together 1 through 9 pandigital.
    '''
    _digits = get_digits(n1)
    _digits.extend(get_digits(n2))
    _digits.extend(get_digits(n3))
    return is_1_9_pandigital(_digits)

def is_1_9_pandigital(digits):
    '''
    Checks if a list of numbers is 1 throught 9 pandigital.
    '''
    if len(digits) != 9: return False
    _set = set([0])
    for i in digits:
        if i in _set: return False
        _set.add(i)
    return True

def get_digits(N):
    '''
    Breaks a number down to a list of it's digits.
    '''
    _digits = []
    while (N > 0):
        N, _digit = divmod(N, 10)
        _digits.append(_digit)
    return _digits

def find_pandigital_products():
    '''
    Finds all pandigital products.
    '''
    _pandigital_products = set()
    for i in range(2, 99):
        _start = 1234 if i < 10 else 123
        for j in range(_start, 10000 // i + 2):
            k = i * j
            if is_1_9_pandigital_group(i, j, k):
                _pandigital_products.add(k)
                #print i, "x", j, "=", k 
    print "Sum:", sum(_pandigital_products)


###############################################################################
# Using strings
def find_pandigital_products_strings():
    '''
    Faster implementation using strings.
    '''
    _pandigital_products = set()
    for i in range(2, 99):
        _start = 1234 if i < 10 else 123
        for j in range(_start, 10000 // i + 2):
            if is_pandigital(str(i * j) + str(i) + str(j)): 
                _pandigital_products.add(i*j)
    print 'Sum:', sum(_pandigital_products)

def is_pandigital(product):
    '''
    Checks if a string is 1-9 pandigital
    '''
    if len(product) != 9: return False
    _set = set('0')
    for k in product:
        if k in _set: return False
        _set.add(k)
    return True

def main():
    StopWatch.start()
    find_pandigital_products()
    StopWatch.print_time()

    StopWatch.start()
    find_pandigital_products_strings()
    StopWatch.print_time()

if __name__ == "__main__": main()