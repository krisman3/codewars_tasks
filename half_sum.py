n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for j in numbers:
    current_sum = 0
    for k in numbers:
        if k == j:
            pass
        else:
            current_sum += k
            
    if current_sum == j:
        print("Yes")
        print("Sum = ", j)
    # else:
    #     current_max = max(numbers)
    #     rest_of_sum = 0
    #     for z in numbers:
    #         if z == current_max:
    #             pass
    #         else:
    #             rest_of_sum += z
    #     print("No")
    #     print(f"Diff = {current_max - rest_of_sum}")