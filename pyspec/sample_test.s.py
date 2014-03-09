from pyspec import end

def test_Burger():
    def apply_ketchup():
        
        def with_ketchup():
            
            def before():
                burger = Burger.new(ketchup = True)
                burger.apply_ketchup()
            end(before)

            it("sets the ketchup flag to true")
            def spec():
                burger.has_ketchup_on_it().should.be_true()
            end(spec)
        
        end(with_ketchup)


        def without_ketchup():
            
            def before():
                burger = Burger.new(ketchup = False)
                burger.apply_ketchup
            end(before)

            it("sets the ketchup flag to false")
            def spec():
                burger.has_ketchup_on_it().should.be_false()
            end(spec)
            
        end(without_ketchup)

    end(apply_ketchup)
end(test_burger)


