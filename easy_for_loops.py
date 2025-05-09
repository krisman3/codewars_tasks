n = int(input())


left_list = []
right_list = []
for i in range(n):
    left_list.append(int(input()))
    right_list.append(int(input()))
    
left = sum(left_list)
right = sum(right_list)

print(f'left: {left} / right: {right}')

if left == right:
    print(f'Yes, sum = {left+right}')
else:
    if left > right:
        print(f'No, diff = {left - right}')
    else:
        print(f'No, diff = {right - left}')

