import random, math

def permute(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    # Recurse
    else:
        
        # for every letter in string
        for i, letter in enumerate(s):
   
            # For every permutation resulting from Step 2 and 3
            for permutation in permute( s[:i] + s[i+1:] ) :
 
                out += [letter + permutation]
            
    return out
