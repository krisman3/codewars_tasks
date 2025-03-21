"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once
(case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""
import unittest


def is_pangram(st: str):
    alphabet_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z'}
    filtered_st = [let.lower() for let in st if let.isalpha()]
    return set(filtered_st) == alphabet_set


class TestFullAlphabet(unittest.TestCase):
    def test_first_string(self):
        self.assertTrue(is_pangram("The quick brown fox jumps over the lazy dog"))
        self.assertTrue(is_pangram('Pack my box with five dozen liquor jugs.'))


if __name__ == "__main__":
    is_pangram("The quick brown fox jumps over the lazy dog")
