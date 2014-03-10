

def run_tests(specs):
    if type(specs) == list:
        for spec in specs:
            if spec["name"] == "spec":
                print run_test(spec)
            elif "tree" in spec:
                run_tests(spec["tree"])

def run_test(spec):
    result = ""
    if "description" in spec:
        description = spec["description"]
    else:
        description = spec["name"]
    try:
        spec["func"]()
        result = ("PASS: Test \"%s\"" % description)
    except Exception as e:
        result = ("FAIL: Test \"%s\"\n\t%s" % (description, str(e)))
    return result
