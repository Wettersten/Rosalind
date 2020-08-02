from basics import nucl_to_aa

file = 'rosalind_ba4a.txt'
out_file = 'out_rosalind_ba4a.txt'

rna_seq = ''
prot = ''

with open(file) as f:
    for line in f:
        rna_seq += line.rstrip()

for i in range(0, len(rna_seq)-3, 3):
    prot += nucl_to_aa(rna_seq[i:i+3])

out_f = open(out_file, 'w')
out_f.write(prot)
out_f.close()

# print(prot)
