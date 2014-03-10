import pyspec
pyspec_import("test_runner")
from test_runner import run_tests
from mock import MagicMock


def test_runner_spec():
    def empty_specs_list_given():
           pass 
    end()
    def spec_in_specs_list():
        
        it("runs spec without description")
        def spec():
            mf = MagicMock()
            specs = [{"name":"spec", "func":mf}]
            run_tests(specs)
            assert mf.called
        end()
        
        it("runs spec with description")
        def spec():
            mf = MagicMock()
            specs = [{"name":"spec", "description": "mock spec", "func":mf}]
            run_tests(specs)
            assert mf.called
        end()
    end()
    def tree_in_specs_list():
        mf = MagicMock()
        specs = [{"name":"spec", "func":mf}]
        #TODO: add spec
    end()
end()




