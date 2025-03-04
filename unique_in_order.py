def unique_in_order(sequence):
    new_string = ''
    for i in sequence:
        if i not in new_string:
            new_string += i
        else:
            continue
    return new_string


if __name__ == "__main__":
    print(unique_in_order("AAAABBBCCDAABBB"))
