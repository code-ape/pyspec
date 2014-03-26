from inspect import ismethod
from pyspec2.spec_tree import SpecTree

def CreateSpecTree(*args, **kwargs):
    if args_not_test_func(*args, **kwargs):
        f = args[0]
        st = SpecTree()
        def wrapped_f(*args_2, **kwargs_2):
            new_args = args_2 + (st,)
            f( *new_args , **kwargs_2 )
        wrapped_f.__name__ = f.__name__
        return wrapped_f
    else:
        st = SpecTree(*args, **kwargs)
        return CreateSpecTree(st)

def args_not_test_func(*args, **kwargs):
    if not ( len(args) == 1 and len(kwargs) == 0 ): return True
    x = args[0]
    if not ismethod(x): return True
    if isinstance(b.im_class, TestCase): return True
    return False
