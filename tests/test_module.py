
import unittest


class UnitTests(unittest.TestCase):
    maxDiff = None

    def test(self):
        actual = "true"
        expected = "true"
        self.assertEqual(actual, expected, 'Is Equal')
        
if __name__ == "__main__":
    unittest.main()
