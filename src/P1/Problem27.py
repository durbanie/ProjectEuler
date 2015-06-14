'''

Problem: Considering quadratics of the form:

n^2 + a*n + b, where |a|, |b| < 1000

find the product of coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting 
with n = 0.

Strategy: Brute Force

Notes: Some notes on the formula:

    n = 0: q = b. Therefore, b must be prime
    n = 1: q = 1 + a + b    
    
    clearly, n^2 + n*a is even for even ns, so b != 2. Thus b is odd and a must
    be odd for q to be odd for all odd n
    
    also, for n = 1, we have 1 + a + b >= 0 => a >= 1-b
    This would give an even number (since b is an odd prime), so instead, use
    a >= -b
    
    Thus, we can limit our search to odd a >= - b and prime b

Runtime: 250 ms

'''

from Common.stopwatch import StopWatch
from Common.prime import Prime

def main():
    StopWatch.start()
    a, b = largest_num_primes()
    print a*b
    StopWatch.print_time()

def test_a_b(a, b, prime):
    '''
    Counts the number of primes given a and b
    '''
    count = 0
    n = 0
    while (True):
        q = n**2 + a*n + b
        if q < 2: break
        if prime.is_prime(q):
            count += 1
            n += 1
        else:
            break
    return count

def largest_num_primes():
    '''
    Finds the combination of a and b which gives the largest number of 
    consecutive primes.
    '''
    _prime = Prime()
    max_count, max_a, max_b = 0, 0, 0
    bs = [x for x in _prime.get_primes(1000)[1:]] # ignore 2
    for b in bs:
        for a in range(-b, 1001, 2):
            count = test_a_b(a, b, _prime)
            if count > max_count:
                max_count, max_a, max_b = count, a, b
    print max_count, max_a, max_b
    return max_a, max_b
    
if __name__ == '__main__':
    main()