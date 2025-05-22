actor_name = input()
points = float(input())
n = int(input())

for _ in range(n):
    letters_in_judge_name = 0
    judge_name = input()
    for letter in judge_name:
        letters_in_judge_name += 1
    judge_points = float(input())
    judge_points = points + ((judge_points * letters_in_judge_name) / 2) #(float(input()) * letters_in_judge_name) + points
print(f'2. {letters_in_judge_name}')
print(f'3. {judge_points}')


if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {judge_points:.2f}!")
else:
    print(f"Sorry, {actor_name} you need {1250-judge_points:.2f} more!")
