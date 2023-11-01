def makeChange(x, coins):
    """
    x: value I want to make change for
    coins: a list of possible coins
    """
    rem = x
    coins = sorted(coins)
    coins.reverse()
    counts = {c: 0 for c in coins}
    while rem > 0:
        for c in coins:
            if c <= rem:
                counts[c] += 1
                rem -= c
                break
    return counts
#|%%--%%| <6JpvVgNOzj|jlmu9spAvA>


coins = [1, 5, 10, 25]

makeChange(41, coins)


#|%%--%%| <jlmu9spAvA|OgvwaPCWjK>
r"""°°°
Subproblems: All possible values <= x
prib[v] the fewest number of coins I need to make change out of v

prob[7] = 1
prob[8] = 2

BaseCase:
prob[0] = 0
°°°"""
#|%%--%%| <OgvwaPCWjK|sjm5JWpF08>

import numpy as np 

#|%%--%%| <sjm5JWpF08|rkK52r7v0m>


def make_change_dyn(x, coins):
    best = np.zeros(x+1)
    choices = np.zeros(x+1)

    for i in range(x+1):
        best[i] = i
        choices[i] = i
    ## Bottom up approach
    for i in range(1, x+1):
        for c in coins:
            if c <= i:
                sol = 1 + best[i-c]
                if sol < best[i]:
                    best = sol


