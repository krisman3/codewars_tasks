n = int(input())


left_list = []
right_list = []

for i in range(n):
    left_list.append(int(input()))
for i in range(n):
    right_list.append(int(input()))
    
left = sum(left_list)
right = sum(right_list)

if left == right:
    print(f'Yes, sum = {left}')
else:
    if left > right:
        print(f'No, diff = {left - right}')
    else:
        print(f'No, diff = {right - left}')
