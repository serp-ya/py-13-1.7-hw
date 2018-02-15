from Animal import Animal

class Mammal(Animal):
    has_teeth = True
    has_fur = True
    has_mammary_gland = True
    has_diaphragm = True
    milk = 0

    def give_a_birth(self, super_class, sex, weight):
        self.milk += 10
        return super().give_a_birth(super_class, sex, weight)


    def wet_nurse(self, child):
        if self.milk:
            doseCount = 1
            self.milk -= doseCount
            dose = {
                'protein': 4.8 * doseCount, # примерная пищевая ценность молока
                'carbohydrate': 7.8 * doseCount,
                'fat': 4.1 * doseCount
            }
            child.feed(dose)