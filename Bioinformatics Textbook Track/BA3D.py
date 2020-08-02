# from collections import OrderedDict

file = 'rosalind_ba3d.txt'
out_file = 'out_rosalind_ba3d.txt'


def debruijn(kmers, seq, k):
    """Takes a list of kmers and DNA sequence, then returns a overlap graph in
    the form of a dictionary. Using the kmers to find all adjacent kmers in dna
    """
    results = {}

    for kmer in kmers:
        adj_kmers = []
        for i in range(len(seq)-k+1):
            curr_kmer = seq[i:i+k-1]
            # print(kmer, curr_kmer)
            if kmer == curr_kmer:
                adj_kmers.append(seq[i+1:i+k])
        results[kmer] = adj_kmers

    return results


def kmer_list(seq, k):
    """Takes dna and returns all kmers from the sequence with k-length of k-1.
    Returns in the form of a list of all kmers, sorted lexicographically.
    """
    kmers = []

    for i in range(len(seq)-k+1):
        curr_kmer = seq[i:i+k-1]
        if curr_kmer not in kmers:
            kmers.append(curr_kmer)

    kmers.sort()
    return kmers


k = 0
seq = ''
kmers = []
results = {}

with open(file) as f:
    k = int(f.readline().rstrip())
    for line in f:
        seq += line.rstrip()

# print(k, seq)
results = debruijn(kmer_list(seq, k), seq, k)
# print(results)

out_f = open(out_file, 'w')
for key in results:
    adjacents = ''
    for adj in results[key]:
        adjacents += adj + ','
    out_f.write('{} -> {}\n'.format(key, adjacents[:-1]))
out_f.close()
