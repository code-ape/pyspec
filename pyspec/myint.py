class something():
    def __init__(self, obj):
        self.obj = obj
    def be_true(self):
        assert self.obj.real == True
    def be_false(self):
        assert self.obj.real == False
    def equal(self, val):
        assert self.obj.real == val


class MyInt(int):
    def __new__(cls, value):
        new_myint = super(MyInt, cls).__new__(cls, value)
        return new_myint
    def __init__(self, value):
        self.should = something(self.real)
    def __add__(self, x):
        return MyInt(self.real + x)

    #def should(self):
    #    return something(self.real)



