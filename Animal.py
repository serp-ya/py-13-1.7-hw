class Animals:
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