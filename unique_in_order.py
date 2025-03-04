def unique_in_order(sequence):
    if not sequence:
        return []

    new_string = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            new_string.append(sequence[i])

    return new_string


if __name__ == "__main__":
    print(unique_in_order("AAAABBBCCDAABBB"))
