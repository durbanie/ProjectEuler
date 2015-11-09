'''

Problem: If p is the perimeter of a right angle triangle with integral length 
    sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?

Strategy: Every right triangle has 3 sides {x, y, z}. For a given perimeter p,
    there are 3 constraints:
    
    x + y + z = p    and    x^2 + y^2 = z^2
    
    We have 2 equations and 3 unknowns.
    
    Also, by construction the set is ordered from least to greatest, that is:
    
    x <= y <= z
    
    Therefore, we know that x <= p/3. So we can loop from x = 1 to x = p/3 and
    use the other two equations to get y and z, checking to make sure that
    they satisfy:
    
    1) both are integers
    2) x <= y <= z
    
    If they do, we add them to the set for that value of p.

Notes: 

Runtime: 

'''

from Common.stopwatch import StopWatch

def max_sets(max_p):
    best_p = 0
    best_n = 0
    for p in range(3, max_p + 1):
        n = num_sets(p)
        if n > best_n:
            best_n, best_p = n, p
    return best_p, best_n

def num_sets(p):
    '''
    Determines the number of {x, y, z} right triangle integer triplets that 
    have perimeter p.
    '''
    n = 0
    for x in range(1, p/3):
        y, r = calculate_y(x, p)
        if r != 0: continue
        if x > y: continue
        if y > p - x - y: continue
        n += 1
    return n

def calculate_y(x, p):
    return divmod(int(p * (p - 2 * x)), int(2 * (p - x)))

def main():
    '''
    Main entry point.
    '''
    StopWatch.start()
    print max_sets(1000)
    StopWatch.print_time()


if __name__ == "__main__": main()