'''

Problem: Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

Strategy: Brute-force

Notes: Long division w/some pattern tracking. As soon as we repeat the numerator
    we know we have found the end of the loop. Use a hash table to check when 
    the repeat occurs.

Runtime: 75 ms (~45 ms if you optimize just to find the length of the cycle)

'''

from Common.stopwatch import StopWatch

def divide_into_1(x):
    _tracker = {1: 0}
    _value = "0."
    _numerator, _place, _length = 1, 1, 0
    while (_numerator != 0):
        _result, _numerator = divmod(_numerator*10, x)
        _value += str(_result)
        if _tracker.has_key(_numerator):
            _position = _tracker[_numerator] + 2
            _length = len(_value[_position:])
            _value = _value[:_position] + "(" + _value[_position:] + ")"
            _numerator = 0
        elif _numerator != 0:
            _tracker[_numerator] = _place
            _place += 1
    return _length, _value

def find_max_cycle_full(n):
    _max = 0
    _maxi = 0
    _maxv = 0
    for i in range(1, n):
        l, v = divide_into_1(i)
        if l > _max:
            _max = l
            _maxi = i
            _maxv = v
        #print "1 / " + str(i) + "\t" + str(l) + "\t" + str(v)
    print "1/" + str(_maxi), _max, _maxv
        
def divide_into_1_length(x):
    _tracker = {1: 0}
    _numerator, _place, _length = 1, 1, 0
    while (True):
        _result, _numerator = divmod(_numerator*10, x)
        if _tracker.has_key(_numerator):
            return _place - _tracker[_numerator]
        _tracker[_numerator] = _place
        _place += 1

def find_max_cycle_fast(n):
    _max = 0
    _maxi = 0
    for i in range(1, n):
        l = divide_into_1_length(i)
        if l > _max:
            _max = l
            _maxi = i
        #print "1 / " + str(i) + "\t" + str(l) + "\t" + str(v)
    print _maxi

def main():
    
    StopWatch.start()
    find_max_cycle_full(1000)
    StopWatch.print_time()
    
    StopWatch.start()
    find_max_cycle_fast(1000)
    StopWatch.print_time()

    

if __name__ == '__main__':
    main()