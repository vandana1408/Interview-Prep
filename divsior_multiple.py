"""
DIVISOR_MULTIPLE.PY

Given an array of n item values, sort the array in ascending order, first by the frequency of each value,  then by the values themselves.

"""

def get_count(l):
    final_arr = []
    for i in range(len(l)):
        div_count = 0 
        mul_count = 0 
        for j in range(len(l)): 
            # Count number of divisors 
            if l[j] % l[i] == 0 and l[i] != l[j]: 
                div_count += 1 
        
            # Count number of multiples 
            if l[i] % l[j] == 0 and l[i] != l[j]: 
                 mul_count += 1 
            
        # add and store into final array 
        final_arr.append(div_count + mul_count) 
    
    return final_arr

if __name__ == "__main__": 
    print(get_count([1, 3, 4, 2, 6]))