from Mammal import Mammal
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Goat(Mammal):
    has_horns = True
    has_bread = True
    is_considered_a_symbol_of_the_devil = True

goat_girl = Goat('f', get_random_weight(50))
goat_man = Goat('m',  get_random_weight(70))

goat_girl.reproduce(goat_man)

kid = goat_girl.give_a_birth(Goat, get_random_sex(), get_random_weight(20))