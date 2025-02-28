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
        pass
    def test_false(self):
        pass
    def test_true2(self):
        pass
    def test_false2(self):

if __name__ == "__main__":
    print(narcissistic(1938))
