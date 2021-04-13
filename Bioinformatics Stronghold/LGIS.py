"""Code for LIS/LDS adapted from https://www.youtube.com/watch?v=4fQJGoeW5VE.
Takes a permutationlist and outputs longest increasing subsequence and longest
decreasing subsequence.
"""


def rosa_input(file):
    n = ''
    perlist = []

    with open(file, 'r') as f:
        n = f.readline().rstrip()
        tmp_list = f.readline().rstrip().split(" ")
        for val in tmp_list:
            perlist.append(int(val))

    return perlist


def lis(d):
    lst = []
    for i in range(len(d)):
        lst.append(max(
            [lst[j] for j in range(i) if lst[j][-1] < d[i]]
            or [[]], key=len) + [d[i]]
        )

    return max(lst, key=len)


def lds(d):
    lst = []
    for i in range(len(d)):
        lst.append(max([lst[j] for j in range(i) if lst[j][-1] > d[i]] or [[]],
                       key=len) + [d[i]])
    return max(lst, key=len)


file = 'rosalind_lgis.txt'
out_file = 'out_rosalind_lgis.txt'
perlist = rosa_input(file)


with open(out_file, 'w') as f:
    inc_list = ""
    dec_list = ""

    for val in lis(perlist):
        inc_list += str(val) + " "
    for val in lds(perlist):
        dec_list += str(val) + " "

    f.write("{}\n".format(inc_list[:-1]))
    f.write("{}\n".format(dec_list[:-1]))
