from Bird import Bird
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Duck(Bird):
    feathers_color = 'green/white'
    fly_away_to_winter = True

duck_girl = Duck('f', get_random_weight(5))
duck_man = Duck('m', get_random_weight(8))

duck_girl.reproduce(duck_man)

duck_child = duck_girl.give_a_birth(Duck, get_random_sex(), get_random_weight(2))