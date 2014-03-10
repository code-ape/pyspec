
class Burger():
    def __init__(self, ketchup=False):
        self.ketchup = ketchup

    def apply_ketchup(self):
        self.ketchup = True

    def has_ketchup_on_it(self):
        return self.ketchup

