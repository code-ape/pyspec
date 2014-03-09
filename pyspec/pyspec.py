
spec_list = []
stack = []

def end(func):
    name = func.__name__
       
    if len(stack) > 0:
        current_root = map_stack(spec_list)
    else:
        current_root = root_spec()
    stack.append(name)
    index = stack.index(name)


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
        func()
    else:
        new_spec = get_item(current_tree, "name", name)
        new_spec["func"] = func

    del stack[index] 
    if stack == []:
        run_tests()

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



def map_stack(specs, stack=stack):
    right_spec = {}
    for spec in specs:
        if spec["name"] == stack[0]:
            right_spec = spec
    if len(stack) > 1:
        return map_stack(right_spec["tree"], stack[1:])
    else:
        return right_spec

def print_tree(level = 0, specs = spec_list):
    for spec in specs:
        if "description" in spec:
            print "  "*level + spec["description"]
            if "name" in spec:
                print "  "*(level+1) + "\\" + spec["name"]
        else:
            print "  "*level + spec["name"]
        if "tree" in spec:
            print_tree(level+1, spec["tree"])


def run_tests(specs = spec_list):
    if type(specs) == list:
        for spec in specs:
            if spec["name"] == "spec":
                run_test(spec)
            elif "tree" in spec:
                run_tests(spec["tree"])

def run_test(spec):
    if "description" in spec:
        description = spec["description"]
    else:
        description = spec["name"]
    try:
        spec["func"]()
        print("PASS: Test \"%s\"" % description)
    except Exception as e:
        print("FAIL: Test \"%s\"" % description)
        print("\t %s" % e)



