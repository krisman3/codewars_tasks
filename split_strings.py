import unittest


def solution(s):
    if not s:
        return []
    i = 0
    j = 2
    str_lst = []
    if len(s) % 2 == 0:
        while i <= len(s):
            while j <= len(s):
                str_lst.append(s[i:j])
                i += 2
                j += 2
            break
    else:
        while i <= len(s):
            while j <= len(s):
                str_lst.append(s[i:j])
                i += 2
                j += 2
            break
        str_lst.append(f"{s[-1]}_")
    return str_lst


class TestStrings(unittest.TestCase):
    def test_evens(self):
        self.assertEqual(solution("asdfadsfas"), ["as", "df", "ad", "sf", "as"])
        self.assertEqual(solution("asdjaskdja"), ["as", "dj", "as", "kd", "ja"])
        self.assertEqual(solution("abcs"), ["ab", "cs"])

    def test_odds(self):
        self.assertEqual(solution("asdfadsfa"), ["as", "df", "ad", "sf", "a_"])
        self.assertEqual(solution("asdjaskdj"), ["as", "dj", "as", "kd", "j_"])
        self.assertEqual(solution("abc"), ["ab", "c_"])


if __name__ == "__main__":
    print(solution("asdfadsfa"))
