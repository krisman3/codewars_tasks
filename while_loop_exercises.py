"""

continuous = True
while continuous:
    word = input()
    if word != 'Stop':
        print(word)
    else:
        continuous = False


##############################

name = input()
password = input()

security = True
while security:
    pass_input = input()
    if pass_input == password:
        print(f"Welcome {name}!")
        security = False
    else:
        continue

##############################


init_max = int(input())
new_num = 0
lower = True

while lower:
    new_num += int(input())
    if new_num >= init_max:
        print(new_num)
        lower = False

##############################

n = int(input())
counter = 1

while counter <= n:
    print(counter)
    counter = counter * 2 + 1

##############################

curr_balance = 0
continuous = True
input_value = ''
while continuous:
    try:
        input_value = float(input())
    except ValueError:
        print(f"Total: {curr_balance:.2f}")
        break
    if float(input_value) > 0:
        curr_balance += float(input_value)
        print(f'Increase: {float(input_value):.2f}')
    elif input_value == 'NoMoreMoney':
        print(f"Total: {curr_balance:.2f}")
        break
    elif input_value <= 0:
        print('Invalid operation!')
        print(f"Total: {curr_balance:.2f}")
        break



##############################


lst_nums = []
data = int(input())
lst_nums.append(data)
while data != 'Stop':
    try:
        data = int(input())
        lst_nums.append(data)
    except ValueError:
        data = 'Stop'
print(max(lst_nums))


##############################


lst_nums = []
data = int(input())
lst_nums.append(data)
while data != 'Stop':
    try:
        data = int(input())
        lst_nums.append(data)
    except ValueError:
        data = 'Stop'
print(min(lst_nums))

##############################
"""

name = input()
strikes = 0
grade = 1
score_list = []

while grade <= 12 or strikes == 2:
    curr_score = float(input())
    if curr_score < 4:
        strikes += 1
        if strikes == 2:
            print(f"{name} has been excluded at {grade} grade")
            break
    elif grade == 12:
        score_list.append(curr_score)
        print(f"{name} graduated. Average grade: {(sum(score_list) / 12):.2f}")
    else:
        score_list.append(curr_score)
        grade += 1
