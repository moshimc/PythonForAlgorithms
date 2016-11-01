import random, math

def permute(s):
    print("CALLED")
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    # Recurse
    else:
        
        # for every letter in string
        print("TOPTOPTOPTOPTOPTOPTOPTOPTOP")
        for i, letter in enumerate(s):
            
            print("--------------------: " + letter + ", " + str(i))
            #print(out)
            #print("reset complete")
            #print(str(i) + ";" + letter)
            print(s[:i] + s[i+1:])
            # For every permutation resulting from Step 2 and 3
            for permutation in permute( s[:i] + s[i+1:] ) :
                print("____________________")
                print(letter + permutation)
                out += [letter + permutation]
                #print("**: " + letter + permutation)
                #print(str(i) + ";{L}:" + letter +";{p}:" + permutation)
                #print(out)
                
    return out
