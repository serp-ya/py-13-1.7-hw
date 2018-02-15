from Bird import Bird
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Chicken(Bird):
    feathers_color = 'white/red'
    fly_away_to_winter = False

chicken = Chicken('f', get_random_weight(2))
cock = Chicken('m', get_random_weight(4))

chicken.reproduce(cock)

cymbals = chicken.give_a_birth(Chicken, get_random_sex(), get_random_weight(0.5))