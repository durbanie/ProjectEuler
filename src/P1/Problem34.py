'''

Problem: 

Find the sum of all the numbers which are equal to the sum of the factorial of 
their digits

Strategy: Brute force.

Notes: The max value that n can possibly have is 7*9! = 2540160. This is 
because if there was an eighth digit, even the sum of the factorial of all 9's 
would have less than 8 digits.

Run-time: 8663 ms

A little long. The last number is 40585. If we can limit to 5 digits instead of
7, we could probably greatly reduce run time.

Upper-bound: https://en.wikipedia.org/wiki/Factorion
The precise upper bound is 1854721, which reduces run time to about 6 s.

'''

from math import factorial

from Common.stopwatch import StopWatch

from Problem30 import getDigits

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    findFactorialSums(1854721)
    StopWatch.print_time()

factorials = {}
def findFactorialSums(max_value):
    '''
    Finds the sum of factorial sums and prints it.
    '''
    global factorials
    factorials = [factorial(n) for n in range(0, 10)]
    _sum = 0;
    for i in range(10, max_value):
        if testNumber(i):
            print i
            _sum += i
    print "Sum:", _sum

def testNumber(N):
    '''
    Tests if a number is a factorial sum.
    '''
    _digits = getDigits(N)
    _factorialSum = sum([factorials[d] for d in _digits])
    return (_factorialSum == N)

if __name__ == '__main__':
    main()