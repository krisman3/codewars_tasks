import random
import unittest

"""
✅ Task 3: Simple Test Case Generator
Difficulty: Mid
Category: File I/O, random, QA relevant

Problem:
Write a script generate_test_cases(n: int, filename: str) that generates a .txt file containing n lines. 
Each line should be a fake test case in the form:
"""


def generate_test_cases(n: int, filename: str):
    with open(filename, 'w') as f:
        for _ in range(n):
            random_num = random.randint(1,1000)
            f.write(f"Input:{random_num} -> Expected Output: {random_num*random_num}\n")
    return


generate_test_cases(0, 'C:\\Users\\KIliev\\PycharmProjects\\Python_Tasks\\temp_files\\testcases.txt')


class TestCasesGenerator(unittest.TestCase):
    def test_3_cases(self):
        filename = 'C:\\Users\\KIliev\\PycharmProjects\\Python_Tasks\\temp_files\\testcases.txt'
        generate_test_cases(3, filename)
        with open(filename, 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 3)

    def test_empty(self):
        pass

    def test_negative(self):
        pass
