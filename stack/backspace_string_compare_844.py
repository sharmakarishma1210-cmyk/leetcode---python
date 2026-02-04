
def backspaceCompare(s , t):
    sstack = []
    tstack = []
    for i in s:
        if i != '#':
            sstack.append(i)
        else:
            if sstack:
                sstack.pop()
    for i in t:
        if i != '#':
            tstack.append(i)
        else:
            if tstack:
                tstack.pop()
    return  sstack == tstack
        
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s , t))

        