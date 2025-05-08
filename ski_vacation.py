days = int(input('How many days: ')) - 1
type_of_room = input('What type of room: ')
review_placed = input('Your review: ')
 
prices = {'room': 18, 'apartment':25, 'president_apartment': 35}
discounts = {'low_apartment': 0.3, 'mid_apartment': 0.35, 'high_apartment': 0.50,
             'low_president': 0.10, 'mid_president': 0.15, 'high_president': 0.20}

reviews = {'positive': 0.25, 'negative': 0.10}
total_cost = 0

if type_of_room == 'room for one person':
    temp_price = prices['room'] * days
    if review_placed == 'positive':
        total_cost = temp_price + (temp_price * reviews['positive'])
        print(f"{total_cost:.2f}") 
    elif review_placed == 'negative':
        total_cost = temp_price - (temp_price * reviews['negative'])
        print(f"{total_cost:.2f}") 
        