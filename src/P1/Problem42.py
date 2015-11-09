'''

Problem: 

Strategy: Brute-force with some memoization

Notes:

Run-time:

'''

from Common.stopwatch import StopWatch

#from Problem22 import letter_score



def count_triangles_in_file(file_name):
    word_list = []
    with open (file_name, "r") as words_file:
        for line in words_file.readlines():
            word_list += line.replace('\"', '').split(',')
    print count_triangles(word_list)

def count_triangles(word_list):
    count = 0
    for word in word_list:
        if is_triangle(calc_value(word)):
            count += 1
    return count

offset = ord('A') - 1
def calc_value(word):
    return sum([ord(c) - offset for c in word.upper()])        

triangle_cache = {}
def is_triangle(num):
    if num in triangle_cache:
        return triangle_cache[num]
    is_tri = calc_n(num).is_integer()
    triangle_cache[num] = is_tri
    return is_tri

def calc_n(num):
    return ((1.0 + 8 * num) ** (0.5)) # - 1) / 2

def main():
    StopWatch.start()
    count_triangles_in_file("p042_words.txt")
    StopWatch.print_time()

if __name__ == '__main__':
    main()