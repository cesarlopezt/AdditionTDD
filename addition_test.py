import unittest
from addition import addition


class TestAdditionMethods(unittest.TestCase):
    def test_2and2equals4(self):
        self.assertEqual(addition(2, 2), 4)

    def test_2and2and2equals6(self):
        self.assertEqual(addition(2, 2, 2), 6)

    def test_emptySumEquals0(self):
        self.assertEqual(addition(), 0)


if __name__ == '__main__':
    unittest.main()
