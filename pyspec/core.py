
import inspect
from test_runner import run_tests
from block import get_block_locals

spec_list = []
call_stack = []
hash_registry = []

def end():
    base_locals = get_block_locals(1)
    test_funcs = clean(base_locals)
    fun = test_funcs.values()[0]
    
    if fun.__hash__() not in hash_registry: 
        hash_registry.append(fun.__hash__())
    name = fun.__name__ 
    if len(call_stack) > 0:
        current_root = map_call_stack(spec_list)
    else:
        current_root = root_spec()
    call_stack.append(name)
    index = call_stack.index(name)


    current_tree = last_tree(current_root)
    current_spec = last_spec(current_root) 
    if current_spec:
        if "description" in current_spec and "name" not in current_spec:
            current_spec["name"] = name 
        elif current_spec:
            current_tree.append({"name": name})
    else:
        current_tree.append({"name": name})    
   
    if name not in ["spec"]:
        if not current_spec:
            current_tree[-1]["tree"] = []
        else:
            new_spec = get_item(current_tree, "name",  name)
            new_spec["tree"] = []
        fun()
    else:
        new_spec = get_item_without_func(current_tree, "name", name)
        new_spec["func"] = fun

    del call_stack[index] 
    if call_stack == []:
        print("")
        print_tree_condensed()
        print("")
        run_tests(spec_list)

def clean(registered_locals):
    return_dict = {}
    avoid = ['__builtins__', '__file__', '__package__', '__name__',
            '__doc__', 'e', 'end', 'l', 'locals', 'it', 'pyspec_import']
    for name, val in registered_locals.items():
        if name not in avoid and inspect.isfunction(val):
            if val.__hash__() not in hash_registry:
                return_dict[name] = val 
    return return_dict



def get_item_without_func(list, key, value):
    for i in list:
        if key in i:
            if i[key] == value and "func" not in i:
                return i 

def get_item(list, key, value):
    for i in list:
        if key in i:
            if i[key] == value:
                return i 

def it(description):
    current_root = root_spec()
    current_spec = last_spec(current_root) 
    current_tree = last_tree(current_root)
    if "description" in current_spec and "name" not in current_spec:
        raise Exception("Tried to add mutliple descriptions")
    else:
        current_tree.append({"description": description})


def root_spec(specs = spec_list):
    if specs == []:
        return None 
    else:
        item = specs[-1]
        loop = True
        while loop:
            loop = False
            if "tree" in item:
                if item["tree"] != []:
                    if "tree" in item["tree"][-1]: 
                        item = item["tree"][-1]
                        loop = True
        return item

def last_spec(current_root):
    if current_root:
        if "tree" in current_root:
            if current_root["tree"] == []:
                return {} 
            else:
                return current_root["tree"][-1]
    else:
        return {}

def last_tree(current_root):
    ret_val = spec_list
    if current_root:
        if "tree" in current_root:
            ret_val = current_root["tree"]
    return ret_val



def map_call_stack(specs, call_stack=call_stack):
    right_spec = {}
    for spec in specs:
        if spec["name"] == call_stack[0]:
            right_spec = spec
    if len(call_stack) > 1:
        return map_call_stack(right_spec["tree"], call_stack[1:])
    else:
        return right_spec

def print_tree(level = 0, specs = spec_list):
    for spec in specs:
        if "description" in spec:
            print "  "*level + spec["description"]
            if "name" in spec:
                print "  "*(level+1) + "\\" + spec["name"].replace("_", " ")
        else:
            print "  "*level + spec["name"].replace("_", " ")
        if "tree" in spec:
            print_tree(level+1, spec["tree"])

def print_tree_condensed(level = 0, specs = spec_list):
    for spec in specs:
        if "description" in spec:
            print "  "*level + spec["description"]
        else:
            print "  "*level + spec["name"].replace("_", " ")
        if "tree" in spec:
            print_tree_condensed(level+1, spec["tree"])





