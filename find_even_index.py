"""
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.
"""


def find_even_index(arr):
    if not arr:
        return -1
    temp_sum_left = 0
    temp_sum_right = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            temp_sum_left += int(arr[i])
            temp_sum_right += int(arr[j])
        if temp_sum_right == temp_sum_left:
            return i + 1
    return f"left: {temp_sum_left} / right: {temp_sum_right}"


if __name__ == "__main__":
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
