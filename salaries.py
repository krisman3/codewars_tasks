websites = {'Facebook': 150, 'Instagram': 100, 'Reddit': 50}
current_websites = []

number_of_tabs_opened = int(input())
salary = float(input())

for _ in range(number_of_tabs_opened):
    if _ in websites:
        salary -= _
    if salary <= 0:
        print("You have lost your salary.")
    else:
        continue

print(salary)

