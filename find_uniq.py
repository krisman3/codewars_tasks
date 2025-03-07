"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""
import unittest


def find_uniq(arr: list):
    unique = arr[0]
    for i in arr:
        if unique != i and arr.count(i) == 1:
            return i
    return unique


class TestUniqueLists(unittest.TestCase):
    def test_uniques(self):
        self.assertEqual(find_uniq([2, 1, 1, 1, 1, 1]), 2)
        self.assertEqual(find_uniq([1, 1, 0.55, 1, 1, 1]), 0.55)
        self.assertEqual(find_uniq([1, 1, 1, 1, 1, 3]), 3)


if __name__ == "__main__":
    print(find_uniq([2, 1, 1, 1, 1, 1]))
