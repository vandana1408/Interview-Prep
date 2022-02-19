"""
IS_POSSIBLE.PY 

Complete the function isPossible in the editor below.

isPossible has the following parameter(s):
    int a:  first value in (a, b)
    int b:  second value in (a, b)
    int c:  first value in (c, d)
    int d:  second value in (c, d)
    
Returns:
    str: Return 'Yes' if (a, b) can be converted to (c, d) by performing zero or more of the operations specified above, or 'No' if not.

"""


def is_possible(a, b, c, d):
    print(a, b, c, d)
    if a > c or b > d: 
        return "No"
    
    if a == c and b == d: 
        return "Yes"
    
    return is_possible(a + b, b, c, d) if a != c else is_possible(a, a + b, c, d)

if __name__ == "__main__": 
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))
    
    print(is_possible(a, b, c, d))
         
        
    