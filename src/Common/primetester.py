'''
Class for testing if a number is prime.
'''

from primesieve import sieveOfEratosthenes
from math import sqrt, ceil

class PrimeTester(object):
    '''
    Tests a number to see if it is prime.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__max = 0
        
    def is_prime(self, num):
        '''
        Checks if the specified number is prime.
        '''
        self.__pre_process__(num)
        max_test = ceil(sqrt(num))
        for n in self.__primes:
            if n > max_test: break
            if num % n == 0: return False
        return True
                
    def __pre_process__(self, num):
        if num > self.__max:
            self.__max = int(ceil(sqrt(num)))
            self.__primes = sieveOfEratosthenes(self.__max)
            

def main():
    '''
    Main entry points for preliminary tests.
    '''
    tester = PrimeTester()
    print tester.is_prime(38290)
    print tester.is_prime(982451653)
    print tester.is_prime(982451650)
    print tester.is_prime(8)
    print tester.is_prime(7)


if __name__ == "__main__": main()