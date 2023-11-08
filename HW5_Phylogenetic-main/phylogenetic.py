import numpy as np
import matplotlib.pyplot as plt
import json
from pandas import *

def load_blosum(filename):
    """
    Load in a BLOSUM scoring matrix for Needleman-Wunsch

    Parameters
    ----------
    filename: string
        Path to BLOSUM file
    
    Returns
    -------
    A dictionary of {string: int}
        Key is string, value is score for that particular 
        matching/substitution/deletion
    """
    fin = open(filename)
    lines = [l for l in fin.readlines() if l[0] != "#"]
    fin.close()
    symbols = lines[0].split()
    X = [[int(x) for x in l.split()] for l in lines[1::]]
    X = np.array(X, dtype=int)
    N = X.shape[0]
    costs = {}
    for i in range(N-1):
        for j in range(i, N):
            c = X[i, j]
            if j == N-1:
                costs[symbols[i]] = c
            else:
                costs[symbols[i]+symbols[j]] = c
                costs[symbols[j]+symbols[i]] = c
    return costs

def needleman_wunsch(s1, s2, costs):
    n = len(s1)
    m = len(s2)

    # make an empty array
    mem = np.zeros((n + 1, m + 1), dtype=int)

    # fill in the base cases 
    for i in range(1, m + 1):
        mem[0, i] = mem[0, i - 1] + costs[s2[i-1]]
            
    for i in range(1, n + 1):
        mem[i, 0] = mem[i - 1, 0] + costs[s1[i-1]]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mem[i, j] = max(mem[i-1, j-1] + costs[s1[i-1]+s2[j-1]], mem[i-1, j] + costs[s1[i-1]], mem[i, j-1] + costs[s2[j-1]])
    #print(DataFrame(mem)) 
    return int(mem[-1, -1])

def needleman_wunsch_all_pairs(species, costs):
    keys = list(species.keys())

    data = {}

    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            data[keys[i] + "," + keys[j]] = needleman_wunsch(species[keys[i]], species[keys[j]], costs)
            print(i)
    print(data)
    return data




#|%%--%%| <pSmRMkbiXA|4LZimNKcwM>

#costs = {"a":-1, "b":-2, "ab":-3, "ba":-3, "aa":2, "bb":3}
#s1 = "aabaab"
#s2 = "ababaa"
costs = load_blosum("HW5_Phylogenetic-main/blosum62.bla")
species = json.load(open("HW5_Phylogenetic-main/organisms.json"))
data = needleman_wunsch_all_pairs(species, costs)
json.dump({"data":data}, open("HW5_Phylogenetic-main/distances.json", "w"))

