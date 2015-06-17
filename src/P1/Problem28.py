'''

Problem:

Starting with the number 1 and moving to the right in a clockwise direction a 5 
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed 
in the same way?

Strategy: Pattern Extrapolation

Notes: Looking at the spiral, first of all, the size of an NxN spiral has 
n=(N+1)/2 concentric circles:

circle 1 = {1}, circle 2 = {2-9}, circle 3 = {10-25}, etc. 

So we want an n = 500 circle spiral. Also note that the nth circle ends with the
value (2*n-1)^2 and asside from the very first circle, each of the other corners
is a sequence of odd numbers skipping every n-2 odd numbers.

For example, for the n=2 circle, we end with (2*2-1)^2 = 9 and skip every 2-2=0
odd numbers (we don't skip any) giving 3, 5, 7, 9.

It can also be seen that if we look at the number we ended with on circle n-1,
we simply skyp n-2 odd numbers to get the first number in circle n's sequence.

For n=3, considering that we ended circle n=2 with 9, and we are skipping 3-2=1
odd number in circle n=3, we know we can start by skipping 11, giving 13. So we 
have 13, 17, 21, 25.

This allows us to build a sequence without squaring.


'''

from Common.stopwatch import StopWatch

def generate_diags(n, last_end):
    '''
    Generates the diagnols for the nth circle given the last ending number.
    '''
    if n == 1:
        return [1]
    seq = []
    skip = 2*(n-1)
    start = last_end + skip
    for i in range(0, 4):
        val = start + i*skip
        seq.append(val)
    return seq
    
def spiral_diagonals(N):
    '''
    Generate the list of diagonals for an NxN spiral
    '''
    n=(N+1)/2
    last_end=0
    diags=[]
    for i in range(1, n+1):
        seq = generate_diags(i, last_end)
        #print seq
        last_end=seq[len(seq)-1]
        diags.extend(seq)
    return diags

def main():
    StopWatch.start()
    print sum(spiral_diagonals(1001))
    StopWatch.print_time()

if __name__ == "__main__": main()