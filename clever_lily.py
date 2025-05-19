age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_amount = 0
birthday_cash = 0
total_birthday_cash = 0
evens = 0
for year in range(1,age+1):
    if year % 2 != 0:
        toys_amount += 1
    elif year % 2 == 0:
        evens += 1
        birthday_cash += 10
        total_birthday_cash += birthday_cash

toy_cash = toys_amount * toy_price
total_cash = (total_birthday_cash + toy_cash) - evens

if washing_machine_price < total_cash:
    print(f"Yes! {total_cash - washing_machine_price:.2f}")
else:
    print(f"No! {abs(total_cash - washing_machine_price)}")

