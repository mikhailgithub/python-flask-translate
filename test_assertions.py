import unittest

class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")

    def test_not_equals(self):
        self.assertNotEqual("one string", "two string")
        
if __name__ == '__main__':
    unittest.main()