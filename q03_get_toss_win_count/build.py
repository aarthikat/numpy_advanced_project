#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution

def get_toss_win_count(team):
    cnt1=[]
    for matches in ipl_matches_array:
        if matches[5]==team:
            cnt1.append(matches[0])
    #rint cnt1
    #print set(cnt1)
    return len(set(cnt1))

get_toss_win_count('Mumbai Indians')
