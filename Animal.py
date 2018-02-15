class Animal:
    it_alive = True
    has_brain = True
    has_heart = True
    has_nervers = True
    weight = 0 # kilograms
    sex = None
    it_pregnant = None

    def feed(self, food):
        self.eat(food)

    def eat(self, food):
        callories = ((food['protein'] * 4) + (food['carbohydrate'] * 4) + (food['fat'] * 9))
        self.digestion(callories, food.poison)

    def digestion(self, callories, poison):
        if poison:
            self.it_alive = False
            print('I died')
        else:
            self.gain(callories)

    def gain(self, callories):
        self.weight += (callories / 1000) # (callories / 1000) for example

    def reproduce(self, partner):
        if self.it_alive and self.sex != partner.sex:
            if self.sex == 'f':
                self.it_pregnant = True
            else:
                partner.it_pregnant = True

    def give_a_birth(self, superClass):
        if self.it_pregnant:
            return superClass()