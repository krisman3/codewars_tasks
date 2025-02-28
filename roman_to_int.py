def romanToInt(s: str):
    """
    :type s: str
    :rtype: int
    """
    dict_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # 'CM': 900, 'CD': 400, 'XC':90, 'XL':40, 'IX':9, 'IV':4

    final_res = 0
    i = 0

    while i < len(s):
        rom_1 = dict_nums[s[i]]

        if i + 1 < len(s):
            rom_2 = dict_nums[s[i + 1]]

            if rom_1 >= rom_2:
                final_res += rom_1
            else:
                final_res += (rom_2 - rom_1)
                i += 1
        else:
            final_res += rom_1
        i += 1
    return final_res


if __name__ == "__main__":
    print(romanToInt("MCMXCIV"))
