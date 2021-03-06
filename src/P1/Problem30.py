'''

Problem: 

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

Strategy: Brute force.

Notes: The max value that n can possibly have is 6*9^5 = 354294. This is 
because if there was a seventh digit, even the sum of the 5th power of all 
9's would have less than 7 digits.

'''

from Common.stopwatch import StopWatch

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    findPowerSums(5, 354294)
    StopWatch.print_time()

def findPowerSums(p, max_value):
    '''
    Finds all numbers which are equal to the sum of the specified power of 
    their digits.
    '''
    _max = max_value
    _sum = 0;
    for i in range(10, _max):
        if testNumber(i, p):
            print i
            _sum += i
    print "Sum:", _sum

def testNumber(N, p):
    '''
    Tests a number to see if it is a "power sum".
    '''
    _digits = getDigits(N)
    _powerSum = sum([d**p for d in _digits])
    return (_powerSum == N)

def getDigits(N):
    '''
    Breaks a number down to a list of it's digits.
    '''
    _digits = []
    while (N > 0):
        N, _digit = divmod(N, 10)
        _digits.append(_digit)
    return _digits

if __name__ == '__main__':
    main()