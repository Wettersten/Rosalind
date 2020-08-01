"""Problem: http://rosalind.info/problems/prob/
Solution: uses gc content to calculte chances for either A/T or G/C, then just
adds those probabilities together and uses common logarithm on the result.
Final results is to be returned with 3 floating digits.
"""
import math
file = 'rosalind_prob.txt'
out_file = 'out_rosalind_prob.txt'
seq = ''
gcs = ''
com_log = ''

with open(file) as f:
    seq = f.readline().rstrip()
    gcs = f.readline().rstrip()

for gc in gcs.split(" "):
    gc_cont = float(gc)
    gc_prob = gc_cont / 2
    at_prob = (1 - gc_cont) / 2
    curr_prob = 1

    # print(gc_cont)
    for nucl in seq:
        if str(nucl) in ['A', 'T']:
            curr_prob = curr_prob * at_prob
        elif str(nucl) in ['G', 'C']:
            curr_prob = curr_prob * gc_prob

        # print(nucl, curr_prob)

    com_log = '{} {:.3f}'.format(com_log, math.log10(curr_prob))

out_f = open(out_file, 'w')
out_f.write(com_log[1:])
out_f.close()

# print(com_log)
