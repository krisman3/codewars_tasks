"""
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even
numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""


def sort_array(source_array):
    new_array = []
    final_array = []
    for i in source_array:
        if i % 2 != 0:
            new_array.append(i)
            source_array.remove(i)
    new_array = sorted(new_array)

    for j in range(len(source_array)):
        try:
            final_array.append(new_array[0])
            final_array.append(source_array[0])
            new_array.pop(0)
            source_array.pop(0)
            j += 1
        except IndexError:
            pass
    print(final_array)

if __name__ == "__main__":
    sort_array([7,1])
