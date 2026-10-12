import math
import random

def normalize(state):
    norm = math.sqrt(sum(abs(a)**2 for a in state))
    if norm == 0:
        raise ValueError('zero state')
    return [a/norm for a in state]

def bell_state():
    s = 1/math.sqrt(2)
    return [s, 0j, 0j, s]

def sample_measurement(probabilities, seed=None):
    rng=random.Random(seed)
    x=rng.random(); total=0.0
    for i,p in enumerate(probabilities):
        total += p
        if x < total: return i
    return len(probabilities)-1
