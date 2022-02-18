"""
ALPHABET_FILTER.PY 

For a given definition of a class LetterFilter, complete its methods filter_vowels and filter_consonants. The class takes a string in the constructor and stores it to its s attribute. 
The method filter_vowels must return a new string with all vowels removed from it. Similarly, the method filter_consonants must return a new string with all consonants removed from it.

"""

class LetterFilter(): 
    def __init__(self, s):
        self.string = s.lower()
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def filter_vowels(self):
        return ''.join([i for i in self.string if i not in self.vowels]) 
        
        
    def filter_consonants(self): 
        return ''.join([i for i in self.string if i in self.vowels])

if __name__ == "__main__":
    string_f = LetterFilter(input("Enter String: "))
    
    print(f'{string_f.filter_vowels()}, {string_f.filter_consonants()}')


