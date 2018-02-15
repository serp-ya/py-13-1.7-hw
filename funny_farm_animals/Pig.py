from Mammal import Mammal
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Pig(Mammal):
    has_fur = False
    likes_dirt = True

pig_girl = Pig('f', get_random_weight(150))
pig_man = Pig('m',  get_random_weight(220))

pig_girl.reproduce(pig_man)

piglet = pig_girl.give_a_birth(Pig, get_random_sex(), get_random_weight(40))