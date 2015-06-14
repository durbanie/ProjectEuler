################################################################################
'''

Problem: Evaluate the sum of all the amicable numbers under 10000.

Strategy: Algorithms/data-structures

Notes: Magic is in the "divisors" method in common.py

Run-time: 156 ms

'''

from Common.myutils import divisors
from Common.stopwatch import StopWatch

def amicable_nums(n):
    """Returns a list of all amicable numbers less than n"""
    _amicable_nums = []
    _sums = [sum(divisors(i)) for i in range(n)]
    for i, val in enumerate(_sums):
        if i == val: continue
        if val < len(_sums) and _sums[val] == i:
            _amicable_nums.append(i)
    return _amicable_nums

def sum_amicable_nums(n):
    """Calculates the sum of all amicable numbers less than n"""
    _amicable_nums = amicable_nums(n)
    return sum(_amicable_nums)

def main():
    StopWatch.start()
    print sum_amicable_nums(10000)
    StopWatch.print_time()

if __name__ == '__main__':
    main()