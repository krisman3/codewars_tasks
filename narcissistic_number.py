def narcissistic(value):
    str_int = str(value)
    num_length = len(str_int)
    powered_full_num = 0
    summed = []
    if num_length == 0:
        return False
    for i in str_int:
        summed.append(int(i) ** num_length)

    return value == sum(summed)

if __name__ == "__main__":
    print(narcissistic(1938))
