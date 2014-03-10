import bowling
import pyspec

@pyspec
class Book():
    
    def before_each(self):
        self.book = Book("Title", "Author", "Category")

    class new():
        

    

def Burger():
    def apply_ketchup():
        def with_ketchup():
            def before():
                burger = Burger.new(ketchup = True)
                burger.apply_ketchup()

                it("sets the ketchup flag to true")
                def spec():
                    burger.has_ketchup_on_it().should.be_true()
                end(spec)
            end(before)
        end(with_ketchup)


        def without_ketchup:
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


describe Burger do
    describe "#apply_ketchup" do
        context "with ketchup" do
            before do
                @burger = Burger.new(:ketchup => true)
                @burger.apply_ketchup
            end

            it "sets the ketchup flag to true" do
                @burger.has_ketchup_on_it?.should be_true
            end
        end

        context "without ketchup" do
            before do
                @burger = Burger.new(:ketchup => false)
                @burger.apply_ketchup
            end

            it "sets the ketchup flag to false" do
                @burger.has_ketchup_on_it?.should be_false
            end
        end
    end
end


describe Book do
    before :each do
        @book = Book.new "Title", "Author", :category
    end

    describe "#new" do
        it "returns a new book object" do
            @book.should be_an_instance_of Book
        end

        it "throws an ArgumentError when given fewer than 3 parameters" do
            lambda { Book.new "Title", "Author" }.should raise_exception 
                                                        ArgumentError
        end
    end
end
