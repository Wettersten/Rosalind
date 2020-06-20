from math import factorial #needed for factorials
#using factorial(x) gives x!
#see http://onlinestatbook.com/2/probability/permutations.html

#Number of permutations is n / n-k. Modulo 100000 by rosalind
def number_permutations(n, k):
    return factorial(n)/factorial(n-k) % 1000000

print(number_permutations(80, 9))