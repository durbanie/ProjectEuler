'''
My stopwatch implementation.
'''

from datetime import datetime

class StopWatch:
    '''
    Stop watch used for timing algorithms.
    '''
    __start = 0
    
    @classmethod
    def start(cls):
        '''
        Starts the clock.
        '''
        cls.__start = datetime.now()
        
    @classmethod
    def get_time(cls):
        '''
        Gets the time as a timespan object.
        '''
        return datetime.now() - cls.__start
    
    @classmethod
    def print_time(cls):
        '''
        Prints the time difference, usually in milliseconds, but in 
        microseconds if less than 1 ms.
        '''
        _td = cls.get_time()
        _tdms = _td.days*86400000 + _td.seconds*1000 + \
            _td.microseconds/1000
        if (_tdms > 0):
            print _tdms, "ms"
        else:
            cls.print_time_us(_td)
    
    @classmethod
    def print_time_us(cls, td = None):
        '''
        Prints the time in microseconds.
        '''
        if (td):
            _tdms = td.days*86400000000 + td.seconds*1000000 + \
                td.microseconds
        else:
            _td = cls.get_time()
            _tdms = _td.days*86400000000 + _td.seconds*1000000 + \
                _td.microseconds
        print _tdms, "us"

def main():
    print "start"
    StopWatch.start()
    for i in range(0, 100000000):
        if i % 10000000 == 0:
            print i
    StopWatch.print_time()
    print "done."
    
if __name__ == "__main__": main()