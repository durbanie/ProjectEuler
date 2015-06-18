'''
Class is here to generate a list of prime numbers up  to some limit. This is 
needed often in Project Euler problems, and it is likely that the 
implementation of this class will change.
'''

from math import sqrt

class Prime(object):
    '''
    Generates prime numbers up to some limit. Caches the set of primes for 
    potential future use.
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.reset()
    
    def reset(self):
        '''
        Reinitializes the max and prime sets.
        '''
        self.__max = 1
        self.__prime_list = []
        self.__prime_set = set([])
    
    def get_first_N_primes(self, N):
        '''
        Finds and returns the list of the first N primes.
        '''
        if len(self.__prime_list) < N:
            self.__find_first_N_primes(N)
        return self.__prime_list
    
    def get_primes(self, N):
        '''
        Returns the list of primes (at least) up to the maximum value of N.
        '''
        if N < self.__max:
            return self.__prime_list
        return self.__find_primes(N)
    
    def is_prime(self, n):
        '''
        Checks if the number n is in the prime set. If n is greater than the 
        max in the set, updates the set.
        '''
        if (n > self.__max):
            self.__find_primes(n)
        return n in self.__prime_set
        
    def __add_prime(self, n):
        self.__prime_list.append(n)
        self.__prime_set.add(n)
    
    def __find_primes(self, N):
        _start = self.__max+1
        for n in range(_start, N+1):
            # check if i is prime directly
            if self.__is_prime(n):
                self.__add_prime(n)
        self.__max = N
        return self.__prime_list
    
    def __find_first_N_primes(self, N):
        n = self.__max
        while (len(self.__prime_list) < N):
            n += 1
            if self.__is_prime(n):
                self.__add_prime(n)
            self.__max = n
        return self.__prime_list
    
    def __is_prime(self, n):
        _sqrtn = sqrt(n)
        for j in self.__prime_list:
            if j > _sqrtn: break
            if n % j == 0: return False
        return True

def main():
    '''
    Main entry points for preliminary tests.
    '''
    print_primes()
    check_up_to_N(100)
    check_up_to_N(2000000)
    get_Nth_prime(10001)
    sum_primes_up_to_N(2000000)

def sum_primes_up_to_N(N):
    from stopwatch import StopWatch
    StopWatch.start()
    _generator = Prime()
    _primes = _generator.get_primes(N)
    print sum(_primes)
    StopWatch.print_time()
    

def get_Nth_prime(N):
    from stopwatch import StopWatch
    StopWatch.start()
    _generator = Prime()
    _primes = _generator.get_first_N_primes(N)
    print _primes[N-1]
    StopWatch.print_time()
    
def check_up_to_N(N):
    from stopwatch import StopWatch
    StopWatch.start()
    _checker = Prime()
    #_checker.get_primes(N)
    for i in range(N):
        if i % 10000 == 0: print i
        if _checker.is_prime(i):
            if N < 10000:
                print i, 
    print ""
    StopWatch.print_time()    

def print_primes(N=100):
    '''
    Prints primes up to 100
    '''
    _generator = Prime()
    print _generator.get_primes(N)

if __name__ == "__main__":
    main()



#     
# from time import time
# def sieve(end):  
#     if end < 2: return []  
# 
#     #The array doesn't need to include even numbers  
#     lng = ((end//2)-1+end%2)  
# 
#     # Create array and assume all numbers in array are prime  
#     sieve = [True]*(lng+1)  
# 
#     # In the following code, you're going to see some funky  
#     # bit shifting and stuff, this is just transforming i and j  
#     # so that they represent the proper elements in the array.  
#     # The transforming is not optimal, and the number of  
#     # operations involved can be reduced.  
# 
#     # Only go up to square root of the end  
#     for i in range(int(end ** .5) >> 1):  
#         if not sieve[i]: continue  
# 
#         # Unmark all multiples of i, starting at i**2  
#         for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
#             sieve[j] = False  
# 
#     # Don't forget 2!  
#     primes = [2]  
#     
#     # Gather all the primes into a list, leaving out the composite numbers  
#     primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  
# 
#     return primes
# 
# startTime = time()
# primes = sieve(2000000)
# total = sum(primes)
# print("Elapsed Time = %f seconds" %(time() - startTime))
# print("the total is %i" %(total))