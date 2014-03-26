

class SpecTree():
    def __init__(self):
        self.root = {}
        self.branch_id_map = {}
        self.spec_id_map = {}
        self.hot_id = 0


    def add_branch(self, name, to_branch = None):
        if to_branch == None:
            id = self.get_id()
            self.root[id] = {"name":name, "branches":{}, }
            self.branch_id_map[id] = self.root[id]
        else:
            target_branch = self.get_branch(to_branch)
            id = self.get_id()
            target_branch["branches"][id] = {"name":name, "branches":{}, }
            self.branch_id_map[id] = target_branch["branches"][id]
        return id


    def get_branch(self, id):
        return self.branch_id_map[id]


    def add_spec(self, to_branch, spec_func = None, it = None):
        if spec_func == None and it == None:
            raise Exception
        branch = self.get_branch(to_branch)
        id = self.get_id()
        if "spec" not in branch:
            branch["spec"] = {}
        
        d = {}
        if spec_func: d["func"] = spec_func
        if it:        d["it"] = it
        branch["spec"][id] = d
        self.spec_id_map[id] = branch["spec"][id] 
        return id

    def update_spec(self, id, spec_func = None, it = None):
        spec = self.get_spec(id)
        if spec_func != None: spec["func"] = spec_func
        if it != None: spec["it"] = it


    def get_spec(self, id):
        return self.spec_id_map[id]
    

    def get_spec_func(self, id):
        return self.get_spec(id)["func"]
    

    def get_id(self):
        response = self.hot_id
        self.hot_id = self.hot_id + 1
        return response
