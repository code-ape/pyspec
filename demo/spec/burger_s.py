
import pyspec
pyspec_import("burger")
from burger import Burger


def test_burger():
    def apply_ketchup():
        it("with ketchup")
        def before():
            burger = Burger(ketchup = True)
            burger.apply_ketchup()

            it("sets the ketchup flag to true")
            def spec():
                assert burger.has_ketchup_on_it() == True 
            end()
        
        end()
        
        def without_ketchup():
            def before():
                burger = Burger(ketchup = False)
            
                it("sets the ketchup flag to false")
                def spec():
                    assert burger.has_ketchup_on_it() == False
                end()
            
            end()
        end()
    
    end()
end()


