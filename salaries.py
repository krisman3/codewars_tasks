websites = {'Facebook': 150, 'Instagram': 100, 'Reddit': 50}

number_of_tabs_opened = int(input())
salary = int(input())

for _ in range(number_of_tabs_opened):
    current_website = input()
    if current_website in websites:
        salary -= websites[current_website]
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)

