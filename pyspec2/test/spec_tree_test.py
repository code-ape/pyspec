from unittest import TestCase, main
from pyspec2.spec_tree import SpecTree
from pyspec2.test.test_utils import CreateSpecTree


class TestSpecTree(TestCase):
    
    def test_initializes_with_name(self):
        st = SpecTree()

    @CreateSpecTree
    def test_initializes_with_empty_root(self, st):
        assert st.root == {}

    @CreateSpecTree
    def test_add_branch_to_root(self, st):
        id = st.add_branch(name = "test_branch")
        assert st.get_branch(id) == {"name":"test_branch", "branches":{}}

    @CreateSpecTree
    def test_add_branch_to_branch(self, st):
        id  = st.add_branch(name = "test_branch")
        id2 = st.add_branch(to_branch = id, name = "test_sub_branch")
        assert st.get_branch(id) == {"name":"test_branch", "branches": {
                                            id2: {"name":"test_sub_branch", "branches":{} },
                                    }}

    @CreateSpecTree
    def test_add_spec_to_branch(self, st):
        id  = st.add_branch(name = "test_branch")
        id2 = st.add_spec(to_branch = id, spec_func = self.mock_speck)
        assert self.mock_speck == st.get_branch(id)["spec"][id2]["func"]

    @CreateSpecTree
    def test_get_spec_by_id(self, st):
        id  = st.add_branch(name = "test_branch")
        id2 = st.add_spec(to_branch = id, spec_func = self.mock_speck)
        assert self.mock_speck == st.get_spec_func(id2)
    
    
    @CreateSpecTree
    def test_add_it_to_branch(self, st):
        id  = st.add_branch(name = "test_branch")
        id2 = st.add_spec(to_branch = id, it = "mock it")
        assert "mock it" == st.get_spec(id2)["it"]
           

    @CreateSpecTree
    def test_update_spec_func(self, st):
        id  = st.add_branch(name = "test_branch")
        id2 = st.add_spec(to_branch = id, spec_func = self.mock_speck)
        st.update_spec(id = id2, spec_func = self.mock_speck_2)
        assert self.mock_speck_2 == st.get_spec_func(id2)
           


    #TODO: raise exception if no args given for add_spec

    
    def mock_speck(self):
        pass

    def mock_speck_2(self):
        pass

if __name__ == "__main__":
    main()
