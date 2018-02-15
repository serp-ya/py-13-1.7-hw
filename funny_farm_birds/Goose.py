from Bird import Bird
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Goose(Bird):
    feathers_color = 'white'
    fly_away_to_winter = True

goose_girl = Goose('f', get_random_weight(7))
goose_man = Goose('m', get_random_weight(10))

goose_girl.reproduce(goose_man)

goose_child = goose_girl.give_a_birth(Goose, get_random_sex(), get_random_weight(4))