
"""
✅ Task 2: Detect Duplicate in List
Difficulty: Junior to Mid
Category: Lists, sets, logic

Problem:
Write a function has_duplicates(items: list) -> bool that checks whether the input list contains any duplicate elements.

Bonus: Modify it to return a list of all duplicates (each only once).
"""
# Working solution, but with higher complexity
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
"""

# Attempt at a single pass + bonus output

def has_duplicates(items: list) -> bool:
    duplicates = {}
    set_duplicates = set()
    for i in items:
        if i not in duplicates.keys():
            duplicates[i] = 1
        else:
            duplicates[i] += 1
            set_duplicates.add(i)
    if set_duplicates:
        print(set_duplicates)
        return True
    return False

        

print(has_duplicates([1, 2, 3, 4, 1, 3, 2]))