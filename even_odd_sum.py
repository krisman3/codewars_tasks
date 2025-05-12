n = int(input())
numbers = []
evens = 0
odds = 0

for i in range(n):
    numbers.append(int(input()))

# odd sum
for i in range(0,len(numbers),2):
    evens += numbers[i]

# even sum
for j in range(1,len(numbers),2):
    odds += numbers[j]

if evens == odds:
    print(f"Yes\nSum = {evens}")
else:
    if evens > odds:
        print(f"No\nDiff = {evens - odds}")
    else:
        print(f"No\nDiff = {odds - evens}")