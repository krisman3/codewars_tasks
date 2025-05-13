n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

found = False 

for j in numbers:
    current_sum = sum(numbers) - j        
    if current_sum == j:
        print("Yes")
        print("Sum =", j)
        found = True
        break

if not found:
    current_max = max(numbers)
    rest_of_sum = sum(numbers) - current_max
    print("No")
    print(f"Diff = {abs(current_max - rest_of_sum)}")