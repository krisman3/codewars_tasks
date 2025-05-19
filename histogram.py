n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

for number in numbers:
    if number < 200:
        p1.append(number)
    elif 200 <= number < 400:
        p2.append(number)
    elif 400 <= number < 600:
        p3.append(number)
    elif 600<= number < 800:
        p4.append(number)
    elif 800 <= number:
        p5.append(number)

print(f"{((len(p1) / n) * 100):.2f}%")
print(f"{((len(p2) / n) * 100):.2f}%")
print(f"{((len(p3) / n) * 100):.2f}%")
print(f"{((len(p4) / n) * 100):.2f}%")
print(f"{((len(p5) / n) * 100):.2f}%")
