
"""
✅ Task 2: Detect Duplicate in List
Difficulty: Junior to Mid
Category: Lists, sets, logic

Problem:
Write a function has_duplicates(items: list) -> bool that checks whether the input list contains any duplicate elements.

Bonus: Modify it to return a list of all duplicates (each only once).
"""


def has_duplicates(items: list) -> bool:
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[j])
    if duplicates:
        return True
    return False

        

print(has_duplicates([1, 2, 3, 4]))