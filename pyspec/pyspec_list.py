expected_list = [
    {'name': 'test_burger'},
    {'name': 'apply_ketchup'},
    {'name': 'with_ketchup'},
    {'name': 'before'},
    {'description': 'sets the ketchup flag to true', 'name': 'spec'},
    {'name': 'without_ketchup'},
    {'name': 'before'},
    {'description': 'sets the ketchup flag to false', 'name': 'spec'},
    ]

def end_list(func):
    name = func.__name__
  
    log("end called with: %s" % name)

    current_spec = last_spec()
    log("current_spec = %s" % str(current_spec))
    if "description" in current_spec and "name" not in current_spec:
        log("added func to current_spec: %s" % name)
        current_spec["name"] = name 
    else:
        log("new spec with func name: %s" % name)
        spec_list.append({"name": name})
    if name not in ["spec", "before"]:
        log("function called from end: %s" % name)
        func()

def it_list(description):
    log("description called with: %s" % description)

    current_spec = last_spec()
    log("current_spec = %s" % str(current_spec))
    if "description" in current_spec and "name" not in current_spec:
        raise Exception("Tried to add mutliple descriptions")
    else:
        log("added DESCRIPTION: %s" % description)
        spec_list.append({"description": description})

'''
def last_spec():
    if spec_list == []:
        return {}
    else:
        return spec_list[-1]
'''

def print_names():
    for name in spec_list:
        print name


