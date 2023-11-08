
def editdyn(s1, s2):
    """
    Parameters
    ----------
    s1: string of length M
        A string with M characters
    s2: string of length N
        A string with N characters
        
    Returns
    -------
    int: The optimal number of add/delete/match/swap
        operations needed to turn s1 into s2 or vice versa
    """

    ## Setup memory (M+1)x(N+1)
    ## mem[i][j] : Edit distance between
    ## first i characters of s1 and
    ## first j characters of s2
    #school
    #fools
    M = len(s1)
    N = len(s2)
    mem = []
    for i in range(M+1):
        mem.append([]) # Add a row
        for j in range(N+1):
            # Add a new column
            mem[i].append(0)
    
    ## Fill in base cases
    for j in range(N+1): # First row
        mem[0][j] = j
    for i in range(M+1):
        mem[i][0] = i
    for i in range(1, M+1):
        for j in range(1, N+1):
            # Delete last character from s1 and match the rest recursively
            case1 = 1 + mem[i-1][j]
            # Delete last character from s2 and match the rest recursively
            case2 = 1 + mem[i][j-1] #
            # Swap or match the last characters from s1 and s2 and match the rest recursively
            case3 = mem[i-1][j-1]
            if s1[i-1] != s2[j-1]: # If last characters are different
                case3 += 1 # Pay for a swap
            mem[i][j] = min(case1, case2, case3)
    x = M 
    y = N
    seq = []
    while x > 0 or y > 0:
        seq.append((x,y))
        
        case1 = 1+mem[x-1][y]
        case2 = 1+mem[x][y-1]
        case3 = mem[x-1][y-1]
        if s1[x-1] != s2[y-1]:
            case3 += 1
        if case1 == mem[x][y]:
            x -= 1
        elif case2 == mem[x][y]:
            y -= 1
        elif case3 == mem[x][y]:
            x -= 1
            y -= 1
    seq.reverse()
            
    return mem[-1][-1], seq # Lower right

    
        
        

# |%%--%%| <R8WARHYyGa|QUEYfHh1qC>

editdyn("school", "fools")
