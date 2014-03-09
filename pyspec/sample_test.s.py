from pyspec import end, it, print_tree


class Burger():
    def __init__(self, ketchup=False):
        self.ketchup = ketchup

    def apply_ketchup(self):
        self.ketchup = True

    def has_ketchup_on_it(self):
        return self.ketchup


def test_burger():
    def apply_ketchup():
        def with_ketchup():
            def before():
                burger = Burger(ketchup = True)
                burger.apply_ketchup()

                it("sets the ketchup flag to true")
                def spec():
                    assert burger.has_ketchup_on_it() == True 
                end(spec)
            
            end(before)
        end(with_ketchup)
        
        def without_ketchup():
            def before():
                burger = Burger(ketchup = False)
            
                it("sets the ketchup flag to false")
                def spec():
                    assert burger.has_ketchup_on_it() == False
                end(spec)
            
            end(before)
        end(without_ketchup)
    
    end(apply_ketchup)
end(test_burger)

print_tree()

expected_tree = [
    {'name': 'test_burger', "tree": [
        {'name': 'apply_ketchup', "tree": [
            {'name': 'with_ketchup', "tree": [
                {'name': 'before'},
                {'description': 'sets the ketchup flag to true', 
                 'name': 'spec'},
            ]},
            {'name': 'without_ketchup', "tree": [
                {'name': 'before'},
                {'description': 'sets the ketchup flag to false', 
                 'name': 'spec'},
            ]}
        ]}
    ]}
]

