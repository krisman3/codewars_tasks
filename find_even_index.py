"""
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.
"""


def find_even_index(arr):
    if not arr:
        return -1

    for i in range(len(arr)):
        temp_sum_left = sum(arr[:i])
        temp_sum_right = sum(arr[i+1:])

        if temp_sum_right == temp_sum_left:
            return i
    return -1


if __name__ == "__main__":
    print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
