import numpy as np
import random
import scipy.stats as ss

def distance(p1: np.array, p2: np.array) -> float:
    """
    Finds the Euclidean distance between points p1 and p2, represented as numpy
    arrays.
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def majority_vote(votes):
    """
    Finds the key which has the most votes in list votes. Returns a random element
    from the list of winners found in the case of ties.
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote in vote_counts:
        if vote_counts[vote] == max_count:
            winners.append(vote)
    return random.choice(winners)

def majority_vote_fast(votes: list):
    """
    Returns the most common element in votes. In case of ties, picks the first winner.
    """
    mode, count = ss.mstats.mode(votes)
    return mode
