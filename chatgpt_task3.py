import random

"""
✅ Task 3: Simple Test Case Generator
Difficulty: Mid
Category: File I/O, random, QA relevant

Problem:
Write a script generate_test_cases(n: int, filename: str) that generates a .txt file containing n lines. 
Each line should be a fake test case in the form:
"""


def generate_test_cases(n: int, filename: str):
    for _ in range(n):
        random_num = random.randint(1,1000)
        with open(filename, 'w') as f:
            f.writelines(f"Input:{random_num} -> Expected Output: {random_num*random_num}\n")
    return


generate_test_cases(3, 'C:\\Users\\KIliev\\PycharmProjects\\Python_Tasks\\temp_files\\testcases.txt')

