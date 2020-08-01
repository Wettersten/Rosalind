file = 'rosalind_ba3a.txt'
k = 0
dna = ''
out_file = 'out_rosalind_ba3a.txt'


def kmer_composition(dna, k):
    """Returns a list of all kmers from kmerComposition(dna), in sequential
    order.
    """
    kmer_list = []

    for i in range(len(dna)-k+1):
        kmer_list.append(dna[i:i+k])

    return kmer_list


with open(file) as f:
    k = int(f.readline().rstrip())
    dna = f.readline().rstrip()

out_list = kmer_composition(dna, k)
results = ''
for kmer in out_list:
    results = results + kmer + '\n'

out_f = open(out_file, 'w')
out_f.write(results)
out_f.close()
