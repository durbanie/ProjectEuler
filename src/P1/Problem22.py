################################################################################
'''

Problem: Using names.txt containing over five-thousand first names, begin by 
    sorting it into alphabetical order. Then working out the alphabetical value 
    for each name, multiply this value by its alphabetical position in the list 
    to obtain a name score. What is the total of all the name scores in the 
    file?
    
Strategy: Algorithms/Data-structures

Notes: Read the names into a list, sort the list (N log(N)), loop over the names
    and then loop over each letter, using a dictionary to get the letter score.
    Finally, sum the product of the scores and indexes. 
    
Runtime: ~15 ms

'''

from Common.stopwatch import StopWatch

letter_score = dict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
})

def score(name):
    """Get the alphabetical score from the name."""
    _score = 0
    for letter in name:
        _score += letter_score[letter]
    return _score

def main():
    
    StopWatch.start()
    
    names = []
    with open ("p022_names.txt", "r") as names_file:
        for line in names_file.readlines():
            line_names = line.replace('\"', '').split(',')
            names.extend(line_names)
    names.sort()
    
    total_score = 0
    for i, name in enumerate(names):
        total_score += (i+1) * score(name)
    print total_score
    
    StopWatch.print_time()

if __name__ == '__main__':
    main()