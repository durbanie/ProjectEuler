'''

Problem: An irrational decimal fraction is created by concatenating the 
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

Strategy: Brute force

Notes: 

Runtime: 

'''

from math import pow
from math import log10

from Common.stopwatch import StopWatch

def find(nmax):
    n, p, d, i = 1, 1, 0, 1
    while n <= nmax:
        di = int(log10(i)) + 1
        if d + di >= n:
            nth_digit = get_nth_digit(i, n - d - 1) 
            p *= nth_digit
            n *= 10
        d += di
        i += 1
    return p

def get_nth_digit(i, n):
    s = str(i)
    return int(s[n])

def numeric_version(max_mult10):
    pwr = int(log10(max_mult10))
    n = [int(pow(10,i)) - 1 for i in range(1, pwr+1)]
    #n = [9, 99, 999, 9999, 99999, 999999, 9999999]
    old_v = 0
    d = 0
    pos = 1
    prod = 1
    for i, v in enumerate(n):
        n_values = v - old_v
        n_digits = (i + 1) * n_values
        while d + n_digits > pos:
            num_to_add, digit_to_get = divmod(pos - d, (i+1))
            num_to_add += old_v
            if digit_to_get == 0:
                prod *= num_to_add % 10
            else:
                prod *= get_nth_digit(num_to_add + 1, digit_to_get - 1)
            pos *= 10
        if pos > max_mult10: break
        d += n_digits
        old_v = v
    return prod

def string_version(max_pow10):
    s = "."
    i = 1
    while len(s) <= max_pow10:
        s += str(i)
        i += 1
    p = 1
    pwr = int(log10(max_pow10))
    n = [int(pow(10,i)) for i in range(1, pwr+1)]
    for i in n:
        p *= int(s[i])
    print p
    return p

def main():
    '''
    Main entry point.
    '''
    max_pow10 = 1000000
    
    #StopWatch.start()
    #print find(max_pow10)
    #StopWatch.print_time()
    
    #StopWatch.start()
    #print string_version(max_pow10)
    #StopWatch.print_time()

    StopWatch.start()
    print numeric_version(max_pow10)
    StopWatch.print_time_us()


if __name__ == "__main__": main()