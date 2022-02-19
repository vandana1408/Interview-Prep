"""
FREQUENCY_SORT.PY

Given an array of n item values, sort the array in ascending order, first by the frequency of each value,  then by the values themselves.

"""
def itemsSort(items):
    elem_count = {}
    for i in items: 
        if i in elem_count: 
            elem_count[i] += 1
        else: 
            elem_count[i] = 1
    
    tuple_list = [(int(i), elem_count[i]) for i in elem_count.keys()] 
    
    tuple_list.sort(key = lambda x: x[1])
    
    final_list = []
    
    for tup in tuple_list: 
        for num in range(tup[1]): 
            final_list.append(tup[0])
            
    return final_list

if __name__ == "__main__": 
    nums = list(input("Enter numbers: ").replace(" ", ""))
    
    print(itemsSort(nums))