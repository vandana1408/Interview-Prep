"""
PERMUTATIONS.PY 

Given an integer string, create all integer permutations of its digits. Determine if there is a permutation whose integer value is evenly divisible by 8, i.e. (permutation value) mod 8 = 0.

"""
def permutations(string): 
    if len(string) <= 1:
        return {string}
    else:
        perms = []
        for i in permutations(string[:-1]):
            for j in range(len(i)+1):
                perms.append(i[:j] + string[-1] + i[j:])
                
        return set(perms) 

def check_divisibility(perms): 
    final = []
    for strings in perms:
        if int(strings) % 8 == 0: 
            final.append('YES')
        else:
            final.append('NO')
    
    return final

if __name__ == "__main__": 
    print(check_divisibility(permutations("1234")))

