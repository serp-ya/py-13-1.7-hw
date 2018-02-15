from Mammal import Mammal
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight

class Cow(Mammal):
    has_horns = True

cow = Cow('f', get_random_weight(400))
bull = Cow('m',  get_random_weight(400))

cow.reproduce(bull)
print('cow is pregnant', cow.it_pregnant)

calf = cow.give_a_birth(Cow, get_random_sex(), get_random_weight(100))
print('calf', calf)
print('calf.sex', calf.sex)
print('calf.weight', calf.weight)

print('cow.milk', cow.milk)
cow.wet_nurse(calf)

print('calf.weight after feed', calf.weight)