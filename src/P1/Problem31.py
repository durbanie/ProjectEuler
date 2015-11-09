'''

Problem:

In England the currency is made up of pound, lb, and pence, p, and there are 
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 lb (100p) and 2 lb (200p).
It is possible to make 2lb in the following way:

1x1lb + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 lb be made using any number of coins?

Strategy: Recursively

Define a function N(v, c) which gives the total number of combinations which 
sum to a value v using denominations fo coins with value less than c.

For example, N(100, 50) gives the total number of combinations using coins of
value 50 or less which sum to a value of 100.

Note that:

N(200, 200) = N(0, 100) + N(200, 100)

That is, to get the total number of combinations to get 200p with coins of 
denomination 200p or less, we can add the cases where we use one 200p coin
and 0 200p coins. 

For the one 200p coin, we have 0p left, so we want the total number of 
combinations to get 0p from coins of denomination of 100p or less. Clearly, 
this is 1 and in general, N(0, c) = 1 for all c.

For the zero 200p coin case, we still have 200p left, so we need the number of
possible cases to get 200p from coins of denomination 100p or less. This is:

N(200, 100) = N(0, 50) + N(100, 50) + N(200, 50)

That is, the sum of cases where we use two, one, and zero 100p coins.

This is clearly a recursive problem. In general:

N(v, c_n) = N(v, c_(n+1)) + N(v-c, c_(n+1)) + N(v-2c, c_(n+1))...

where c_n represents the nth coin denomination (ordered from greatest to least)
and v-mc >= 0.

Wo we just need the base cases. We've already found one of them: 
N(0, v) = 1 for all v.

We also know that for the lowest denomination (1p) we have N(v, 1) = 1 because
there is only one way to get e.g. 100p with 1p coins (i.e. exactly 100 1p 
coins).

'''

from Common.stopwatch import StopWatch

def main():
    StopWatch.start()
    #print N(2000, 0)
    print memoization(200)
    #print memoN(20000, 0)
    StopWatch.print_time()

def N(v, i, coins=[200, 100, 50, 20, 10, 5, 2, 1]):
    '''
    Returns the number of possible combinations to arrange a set of coin
    denominations to sum to a particular value using values less than or equal
    to coins[i]
    '''
    #print "N(" + str(v) + ", " + str(coins[i]) + ")"
    if v < 0: return 0
    if v == 0: return 1
    if i + 1 == len(coins): return 1
    _sum, _n = 0, 0
    while v - _n * coins[i] >= 0:
        _sum += N(v - _n * coins[i], i+1, coins)
        _n += 1
    return _sum

def memoize(f):
    memo = {}
    def helper(x, y):
        if (x, y) not in memo:            
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]
    return helper

denominations=[200, 100, 50, 20, 10, 5, 2, 1]

@memoize
def memoN(v, i):
    if v < 0: return 0
    if v == 0: return 1
    if i + 1 == len(denominations): return 1
    _sum, _n = 0, 0
    while v - _n * denominations[i] >= 0:
        _sum += memoN(v - _n * denominations[i], i+1)
        _n += 1
    return _sum

def memoization(N):
    values=[1,2,5,10,20,50,100,200]
    n=len(values)
    T=[[1]+[0]*N for _ in range(n)]
    print len(T)
    for x in range(1,N+1):
        for j in range(n):
            if x<values[j]:
                T[j][x]=T[j-1][x]
            else:
                T[j][x]=T[j-1][x]+T[j][x-values[j]]
    return (T[-1][-1])

if __name__ == '__main__':
    main()