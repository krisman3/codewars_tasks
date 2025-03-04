import unittest


def unique_in_order(sequence):
    if not sequence:
        return []

    new_string = [sequence[0]]
    for i in range(1, len(str(sequence))):
        if sequence[i] != sequence[i - 1]:
            new_string.append(sequence[i])

    return new_string


class TestDifferentTypes(unittest.TestCase):
    def test_single_item(self):
        self.assertEqual(unique_in_order("A"), ["A"])
        self.assertEqual(unique_in_order([]), [])
        self.assertEqual(unique_in_order(()),[])

    def test_reduce_duplicate(self):
        self.assertEqual(unique_in_order("AA"), ["A"])
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])


if __name__ == "__main__":
    print(unique_in_order("AAAABBBCCDAABBB"))
