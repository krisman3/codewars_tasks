"""
Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
Според размера на групата, катерачите ще изкачват различни върхове.
Група до 5 човека – изкачват Мусала
Група от 6 до 12 човека – изкачват Монблан
Група от 13 до 25 човека – изкачват Килиманджаро
Група от 26 до 40 човека –  изкачват К2
Група от 41 или повече човека – изкачват Еверест
Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

Изход
Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до
втората цифра след десетичната запетая.

Първи ред - процентът изкачващи Мусала
Втори ред – процентът изкачващи Монблан
Трети ред – процентът изкачващи Килиманджаро
Четвърти ред – процентът изкачващи К2
Пети ред – процентът изкачващи Еверест
"""

num_of_groups = int(input())
total_people = 0
people_list = {'Musala': 0, 'Montblanc': 0, 'Kilimangaro': 0, 'k2': 0, 'Everest': 0}
for i in range(num_of_groups):
    num_of_people = int(input())
    total_people += num_of_people
    if num_of_people <= 5:
        people_list['Musala'] += num_of_people
    elif 6 <= num_of_people <= 12:
        people_list['Montblanc'] += num_of_people
    elif 13 <= num_of_people <= 25:
        people_list['Kilimangaro'] += num_of_people
    elif 26 <= num_of_people <= 40:
        people_list['k2'] += num_of_people
    else:
        people_list['Everest'] += num_of_people


print(f"{(people_list['Musala'] / total_people) * 100:.2f}%")
print(f"{(people_list['Montblanc'] / total_people) * 100:.2f}%")
print(f"{(people_list['Kilimangaro'] / total_people) * 100:.2f}%")
print(f"{(people_list['k2'] / total_people) * 100:.2f}%")
print(f"{(people_list['Everest'] / total_people) * 100:.2f}%")

