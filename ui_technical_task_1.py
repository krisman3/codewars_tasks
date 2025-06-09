def fizz_buzz(n):
    fizz = []
    buzz = []
    fizzbuzz = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append(i)
        elif i % 3 == 0:
            fizz.append(i)
        elif i % 5 == 0:
            buzz.append(i)

    # Normally I would just check with len()
    # However, here is the while loop
    fizz_num = 0
    buzz_num = 0
    fizzbuzz_num = 0

    j = 0
    while j < len(fizz):
        fizz_num += 1
        j += 1

    j = 0
    while j < len(buzz):
        buzz_num += 1
        j += 1

    j = 0
    while j < len(fizzbuzz):
        fizzbuzz_num += 1
        j += 1

    return fizz_num, buzz_num, fizzbuzz_num

print(fizz_buzz(15))