VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def filter_vowels(s):
    return ''.join([i for i in s if i not in VOWELS])
    
    
def filter_consonants(s): 
        return ''.join([i for i in s if i in VOWELS])

if __name__ == "__main__":
    string_f = input("Enter String: ")
    
    print(f'{filter_vowels(string_f)}, {filter_consonants(string_f)}')


