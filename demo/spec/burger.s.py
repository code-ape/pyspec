
from pyspec import end, it, target_import 

target_import(burger)


def test_burger():
    def apply_ketchup():
        it("with ketchup")
        def before():
            burger = Burger(ketchup = True)
            burger.apply_ketchup()

            it("sets the ketchup flag to true")
            def spec():
                assert burger.has_ketchup_on_it() == True 
            end(spec)
        
        end(before)
        
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



