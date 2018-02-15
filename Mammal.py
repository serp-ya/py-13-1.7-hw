from Animal import Animal

class Mammals(Animal):
    has_teeth = True
    has_fur = True
    has_mammary_gland = True
    has_diaphragm = True
    milk = 0

    def give_a_birth(self, superClass):
        super().give_a_birth(superClass)
        self.milk += 10

    def wet_nurse(self, child):
        if self.milk:
            milkCount = 1
            self.milk -= milkCount
            child.feed(milkCount)