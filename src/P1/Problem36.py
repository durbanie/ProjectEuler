'''

Problem:
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)



Strategy: Generate all binary or decimal palindromes, check if the other base
is also a palindrome:

NO LEADING Zeros:

Generate binary: 1000000 = 20 bits. Possible palindromes: 2^9 + 2^8 + 2^7 ...
= 1023

Generate decimal: 3 digits: 9*10*10 = 900 + 9*10 + 9 = 999

Slightly less w/decimal, we'll go with that.



Run-time: < 1us

'''

from Common.stopwatch import StopWatch

def count_db_palindromes():
    '''
    Generates a list of decimal palindromes
    '''
    _sum = 0
    for i in range(1, 10):
        if is_binary_palindrome(i):
            _sum += i
    for i in range(1, 1000):
        _pstr = str(i)
        if is_binary_palindrome(int(_pstr + _pstr[::-1])):
            _sum += int(_pstr + _pstr[::-1])
        if len(_pstr) < 3:
            for j in range (0, 10):
                if is_binary_palindrome(int(_pstr + str(j) + _pstr[::-1])):
                    _sum += int(_pstr + str(j) + _pstr[::-1])
    print "Sum:", _sum
    

def is_binary_palindrome(n):
    '''
    Checks if a decimal is a binary palindrome.
    '''
    _binary = bin(n)[2:]
#     if is_palindrome(_binary):
#         print n, "-", _binary
#         return True
#     return False        
    return is_palindrome(_binary)

def is_palindrome(s):
    '''
    Checks if a string is a palindrome
    '''
    _lasti = len(s) - 1
    for i in range(len(s)/2):
        if s[i] != s[_lasti - i]: return False
    return True
    

def main():
    StopWatch.start()
    count_db_palindromes()
    StopWatch.print_time()
    
if __name__ == "__main__": main()

