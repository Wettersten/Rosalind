file = 'rosalind_ba3b.txt'
out_file = 'out_rosalind_ba3b.txt'


def genome_path(file):
    """Returns a list of all kmers from kmerComposition(dna), in sequential
    order.
    """
    dna = ''

    with open(file) as f:
        dna = f.readline().rstrip()
        for seq in f:
            dna += seq.rstrip()[-1]

    return dna


results = genome_path(file)

out_f = open(out_file, 'w')
out_f.write(results)
out_f.close()
