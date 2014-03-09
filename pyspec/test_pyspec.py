import unittest
import pyspec

class TestPyspec(unittest.TestCase):
   
    def setUp(self):
        pyspec.init_spec_list()

    def test_root_spec_empty_list(self):
        pyspec.init_spec_list()
        self.assertEqual(pyspec.get_spec_list(), [])


if __name__ == '__main__':
    unittest.main()
