import math

def entropy(prob):
    eps = 1e-6
    return - (prob * math.log(prob + eps) + (1 - prob) * math.log(1 - prob + eps))

def is_uncertain(prob, low=0.4, high=0.6):
    return low < prob < high
