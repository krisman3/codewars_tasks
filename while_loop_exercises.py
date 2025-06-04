"""

continuous = True
while continuous:
    word = input()
    if word != 'Stop':
        print(word)
    else:
        continuous = False


####

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

init_max = int(input())
new_num = 0
lower = True

while lower:
    new_num += int(input())
    if new_num >= init_max:
        print(new_num)
        lower = False

"""
