def myDecorator(target_f):
    def new_f():
        target_f()
        

@myDecorator
def aFunc():
    print "inside aFunc"

print "Decorator done"

aFunc()

print "All done"
