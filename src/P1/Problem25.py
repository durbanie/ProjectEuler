'''

Problem: Find the index of the first 1000 digit fibonacci number.

Strategy: Brute-force & Mathematical

Notes: Implementing this as an array with each digit as an entry in the array. 
    In Python, this is actually not necessary (python allows an arbitrary number 
    of digits in an integer), but in other languages like C or Java, the number 
    of digits is limited. Therefore, this array implementation is meant to be 
    valid in other languages.
    
    The mathematical strategy involves an approximation to binet's formula,
    where to find the nth fibonacci number F(n):
    
    F(n) = Phi^n / sqrt(5)
    
    where Phi is the golden ratio, Phi = 1.61803398875...
    
    To find the number of digits, take log_10 of F(n) and add 1
    
    Ndigits(F(n)) = n log10(Phi) - log10(sqrt(5)) + 1
    
    Solving for n gives:
    
    n = (Ndigits(F(n)) - 1 + log10(sqrt(5))) / log10(Phi)
       
Run-time: Brute-force: 1435 ms, mathematical: <1us

'''

from math import log10
from Common.stopwatch import StopWatch

def add(l1, l2):
    l3 = []
    r = 0
    l1l = len(l1)
    l2l = len(l2)
    ml = max(l1l, l2l)
    for i in range(ml):
        #print i, l1, l2
        l1v, l2v = 0, 0
        if (i < len(l1)): l1v = l1[i]
        if (i < len(l2)): l2v = l2[i]
        #print l1v, l2v, r
        r, v = divmod(l1v+l2v+r, 10)
        l3.append(v)
    if r > 0:
        #print r 
        l3.append(r)
    return l3

def fibonacci_brute_force():
    i = [1]
    j = [1]
    counter = 1
    while len(j) < 1000:
        counter += 1
        t = j
        j = add(i, j)
        i = t
    print len(j)
    print counter+1

root5 = 2.236068
Phi   = 1.618034
def fibonacci_math(ndigits):
    #n = (Ndigits(F(n)) + log10(sqrt(5))) / log10(Phi)
    return int(round((ndigits - 1 + log10(root5)) / log10(Phi))) 

def main():
    StopWatch.start()
    fibonacci_brute_force()
    StopWatch.print_time()
    
    StopWatch.start()
    print fibonacci_math(1000)
    StopWatch.print_time()

if __name__ == '__main__':
    main()