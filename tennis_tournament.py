number_of_tournaments = int(input())
starting_points = int(input())
total_points = 0
won_tournaments = 0

for i in range(number_of_tournaments):
    stage = input()
    if stage == 'W':
        won_tournaments += 1
        total_points += 2000
    elif stage == 'F':
        total_points += 1200
    elif stage == 'SF':
        total_points += 720

avg_points = total_points // number_of_tournaments
total_points += starting_points

print(f'Final points: {total_points}')
print(f'Average points: {avg_points}')
print(f'{(won_tournaments / number_of_tournaments) * 100:.2f}%')
