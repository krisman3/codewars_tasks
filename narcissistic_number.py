import unittest
def narcissistic(value):
    str_int = str(value)
    num_length = len(str_int)
    powered_full_num = 0
    summed = []
    if num_length == 0:
        return False
    for i in str_int:
        summed.append(int(i) ** num_length)

    return value == sum(summed)


class TestDifferentNumbers(unittest.TestCase):

    def test_true(self):
        self.assertTrue(narcissistic(371), "371 is a narcissistic number")

    def test_false(self):
        self.assertFalse(narcissistic(122), "122 is not a narcissistic number")

    def test_true2(self):
        self.assertTrue(narcissistic(7), "7 is a narcissistic number")

    def test_false2(self):
        self.assertFalse(narcissistic(4887), "4887 is not a narcissistic number")


if __name__ == "__main__":
    unittest.main()
