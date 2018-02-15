import random

def get_random_weight(multiplier = 1):
    random_num = random.random()
    return round(random_num * multiplier, 2)