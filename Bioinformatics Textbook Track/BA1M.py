#Implement PatternToNumber

def read_file(filename):
    with open(filename, 'r') as file:
        index = file.readline().strip()
        k = file.readline().strip()
        
        return int(index), int(k)

def number_to_symbol(number):
    number_dict = {0:"A", 1:"C", 2:"G", 3:"T"}
    return number_dict[number]

def quotient(index, k):
    return int(index/k), int(index%k)


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(int(index))
    prefix_index, r = quotient(index, 4)
    symbol = number_to_symbol(r) #gets the nucl for the last index, saves rest numbers
    prefix_pattern = number_to_pattern(prefix_index, k-1) #loops over prefix
    
    return prefix_pattern + symbol #adds the known last nucl to the end of the loop

index, k = read_file("rosalind_ba1m.txt")
print(number_to_pattern(index, k))