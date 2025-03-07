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


# class TestUniqueLists(unittest.TestCase):
#     def test_uniques(self):
#         self.assertEqual(find_uniq([2, 1, 1, 1, 1, 1]), 2)
#         self.assertEqual(find_uniq([1, 1, 0.55, 1, 1, 1]), 0.55)
#         self.assertEqual(find_uniq([1, 1, 1, 1, 1, 3]), 3)


if __name__ == "__main__":
    print(solution("asdfadsfa"))
