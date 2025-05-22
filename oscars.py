actor_name = input()
points = float(input())
judges = int(input())

judge_points_list = []
for _ in range(judges):
    judge_name = input()
    letters_in_judge_name = len(judge_name)

    judge_points = float(input())
    judge_points_list.append((judge_points * letters_in_judge_name) / 2)
    temp_judge_points = points + sum(judge_points_list) 
    if temp_judge_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {temp_judge_points:.1f}!")
        break

if temp_judge_points < 1250.5: 
    print(f"Sorry, {actor_name} you need {1250.5 - temp_judge_points:.1f} more!")