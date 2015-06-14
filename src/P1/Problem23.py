################################################################################
'''

Problem: Find the sum of all the positive integers which cannot be written as 
    the sum of two abundant numbers.

Strategy: Algorithms/Data-structures

Notes: Use divisors method to determine list of abundant numbers. Create an 
    array of booleans up to the theoretical maximum (28123), which will say
    whether or not the number can be written as the sum of two abundant numbers.
    Initialize the booleans to false. Use a double loop over the abundant 
    numbers to generate the numbers that can be written as the sum of abundant
    numbers, setting the appropriate boolean to true. Then use the boolean array
    to determine the sum.
    
Run-time: 3263 ms

'''

from Common.myutils import divisors
from Common.stopwatch import StopWatch
from enum import Enum

class SumType(Enum):
    '''
    Enumeration for classifying numbers as deficient, abundant, etc.
    '''
    Deficient = -1
    Perfect = 0
    Abundant = 1

def get_type(num):
    '''
    Checks whether a number is deficient, perfect, or abundant and returns the 
    corresponding enumeration.
    '''
    if (num == 0): return SumType.Perfect
    _divs = divisors(num)
    _sum = sum(_divs)
    if (_sum < num):
        return SumType.Deficient
    if (_sum == num): 
        return SumType.Perfect
    return SumType.Abundant

def abundant_numbers(maxn):
    '''
    Returns all abundant numbers up to some specified maximum.
    '''
    _nums = []
    for n in range(maxn):
        if get_type(n) == SumType.Abundant:
            _nums.append(n)
    return _nums

def sum_nonabandant_numbers(maxn):
    '''
    Returns the sum of all non-abundant numbers up to some maximum.
    '''
    _anums = abundant_numbers(maxn)
    
    _canbe = [1 for _ in range(maxn)]
    for i in range(len(_anums)):
        for j in range(i, len(_anums)):
            if (_anums[i]+_anums[j] >= maxn): 
                break
            _canbe[_anums[i]+_anums[j]] = 0
    
    return sum([v*i for i, v in enumerate(_canbe)])
    

def main():
    StopWatch.start()
    
    _max = 28123
    #_max = 20162
    print "Non-abundant sums:", sum_nonabandant_numbers(_max)
    
    StopWatch.print_time()

if __name__ == '__main__':
    main()