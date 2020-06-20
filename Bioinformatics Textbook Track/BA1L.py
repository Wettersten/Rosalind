#Implement PatternToNumber

def read_file(filename):
    with open(filename, 'r') as file:
        dna = file.readline().strip()
        
        return str(dna)

def symbol_to_number(symbol):
    symbol_dict = {"A":0, "C":1, "G":2, "T":3}
    return symbol_dict[symbol]

def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    
    symbol = pattern[-1]
    prefix = pattern[:len(pattern)-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)

print(pattern_to_number(read_file("rosalind_ba1l.txt")))