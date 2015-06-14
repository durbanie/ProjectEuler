"""

Problem: Find the 1,000,000th lexographically-ordered permutation of the digits 
    "0123456789".

Strategy: Mathematical

Notes: Given N digits, you can determine the most significant digit of the kth 
    permutation by dividing k by (N-1)! (the total number of permutations of 
    all other digits). Of the remaining significant digits, we can repeat this 
    process (finding the next significant digit) by finding the k%(N-1)!th 
    permutation of the remaining N-1 digits. 

Consider permutations of "0", "1", "2", and "3" listed below:

0.  0123
1.  0132
2.  0213
3.  0231
4.  0312
5.  0321
6.  1023
7.  1032
8.  1203
9.  1230
10. 1302
11. 1320
12. 2013
13. 2031
14. 2103
15. 2130
16. 2301
17. 2310
18. 3012
19. 3021
20. 3102
21. 3120
22. 3201
23. 3210

There are 4! = 24 such permutations. For 10 numbers, there are 10! = 3,628,800 
total possible permutations.

We can try and "brute force" it, reading the rules of cyclical permutation, 
performing the operations in order to get to 1,000,000. Or, we can compose the 
permutation the following way.

We are looking for the kth permutation in N digits. Start with k0 = k

Start with the 0th digit: n0 = k0  / (N-1)! => take the n0th available spot in 
the list [0, 1, 2, ...]. Then calculate what remains: k1 = k0 % (N-1)!

Next take the 1st digit: n1 = k1 / (N-2)!  =>  take the n1th available spot in 
the list after removing from the previous step and k2 = k1 % (N-1)!

In general, nn = kn / (N-1-n)!, kn-1 = kn % (N-1)!  =>  take the nnth available 
digit.

In the above example, suppose we are looking for the 14th permutation (starting 
with 0)

k0 = 14
n0 = 14 / (4-1)! = 14/6 = 2 => take the 2nd spot in the list [0, 1, 2, 3] = 2
k1 = 14 % (4-1)! = 2
n1 = 2 / (4-2)! = 2/2 = 1 => take the 1st spot in the list [0, 1, 3] = 1
k2 = 2 % (4-2)! = 0
n3 = 0 / (4-3)! = 0 => take the 0th spot in the list [0, 3] = 0
k3 = 0 % (4-3)! = 0
n4 = 0 / 0! = 0 => take the 0th spot in the list [3] = 3

Therefore, the 14th permutation is 2103

"""

from math import factorial

from Common.stopwatch import StopWatch


def get_permutation(N, digit_list):
    '''
    Returns the nth lexographically ordered permutaition given the list of
    ordered
    '''
    _final = ""
    while len(digit_list) > 0:
        _digit, N = get_spot(N, digit_list)
        _final = _final + _digit
    return _final

def get_spot(n, digit_list):
    _N = len(digit_list) - 1
    _Nfac = factorial(_N)
    _index = n / _Nfac
    _remaining = n % _Nfac
    
    if (_index >= len(digit_list)):
        print "Index out of range!"
        digit_list = []
        return '', 0
    
    _digit = digit_list.pop(_index)
    return _digit, _remaining

def main():
    StopWatch.start()
    
    print get_permutation(999999, [str(x) for x in range(10)])
    
    StopWatch.print_time()
        
if __name__ == "__main__": main()