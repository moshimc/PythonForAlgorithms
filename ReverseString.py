def reverse(s):
    
    string = s[-1]
    if len(s) > 1:
        return string + reverse(s[:-1])
    elif len(s) == 1:
        return string
    else:
        return
    
    print(string)

def reverse2(s):
    
    if len(s) > 1:
        return s[-1] + reverse(s[:-1])
    elif len(s) == 1:
        return s[-1]
    else:
        return