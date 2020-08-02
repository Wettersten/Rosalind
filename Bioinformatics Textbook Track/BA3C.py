from collections import OrderedDict

file = 'rosalind_ba3c.txt'
out_file = 'out_rosalind_ba3c.txt'


def overlap_kmers(list):
    """Takes a list and then returns a overlap graph in the form of an
    adjacency list of all kmers, prefix-suffix.
    """
    results = {}
    for kmer in list:
        curr_kmer = kmer
        for overlap in list:
            curr_overlap = overlap
            if kmer is not curr_overlap:
                found1 = False
                found2 = False
                if curr_kmer[:len(curr_kmer)-1] == curr_overlap[1:]:
                    results[curr_overlap] = curr_kmer
                    found1 = True
                if curr_kmer[1:] == curr_overlap[:len(curr_overlap)-1]:
                    results[curr_kmer] = curr_overlap
                    found2 = True
                if found1 and found2:
                    break

    return results


list = []
with open(file) as f:
    for seq in f:
        list.append(str(seq.rstrip()))
results = overlap_kmers(list)
results_sorted = OrderedDict(sorted(results.items()))  # Requires sorted output

out_f = open(out_file, 'w')
for key in results_sorted:
    out_f.write('{} -> {}\n'.format(key, results_sorted[key]))
out_f.close()
