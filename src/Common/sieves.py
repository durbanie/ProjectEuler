'''

Collection of prime sieve methods

'''

#import psyco; psyco.full()
from math import sqrt, ceil

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2) # is there a way we can do this
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2 # index of the square of si
            if bottom >= top:
                break
            num_zeros = -((bottom - top) // si)
            sieve[bottom::si] = [0] * num_zeros
    return [2] + [el for el in sieve if el]

if __name__=='__main__':
    
    n=10000000
    
    from stopwatch import StopWatch
        
    StopWatch.start()
    sieveOfEratosthenes(n)
    print "Sieve of Eratosthenes: ",
    StopWatch.print_time()
    