def readGenome(filename):
    genome = ''
    seqs = []
    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            # ignore header line with genome information
            if line[0] == '>' and len(genome) > 0:
                seqs.append(genome)
                genome = ''
            if not line[0] == '>':
                genome += line.rstrip()
    if len(genome) > 0:
        seqs.append(genome)
    return seqs
    
r_long = readGenome('rosalind_long.txt')

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

import itertools

def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_sup = None
    shortest_list = []
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_list = []
            shortest_sup = sup  # found shorter superstring
            shortest_list.append(sup)
        elif len(sup) == len(shortest_sup):
            shortest_list.append(sup)
    return shortest_list  # return shortest

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a) #removes read a
        reads.remove(read_b) #removes read b
        reads.append(read_a + read_b[olen:]) #makes new merged string
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads) #if multiple left merges all
	
