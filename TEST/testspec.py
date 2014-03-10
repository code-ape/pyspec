import inspect

hash_registry = []
call_stack = []

def end():
    stack = inspect.stack()
    frames = [frame_obj[0] for frame_obj in stack]
    last_frame = frames[1]
    base_locals = last_frame.f_locals
    test_funcs = clean(base_locals)
    print(test_funcs)
    i = test_funcs.values()[0]
    if hasattr(i, '__call__') and i.__hash__() not in hash_registry: 
        print("RUNNING: %s" % str(i))
        hash_registry.append(i.__hash__())
        i()


def clean(registered_locals):
    return_dict = {}
    avoid = ['__builtins__', '__file__', '__package__', '__name__',
            '__doc__', 'e', 'end', 'l', 'locals']
    for i in registered_locals:
        if i not in avoid:
            return_dict[i] = registered_locals[i] 
    return return_dict



