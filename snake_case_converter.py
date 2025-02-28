"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    merged_word = ''
    i = 0
    while i < len(text):
        if text[i] in ['-', '_']:
            if text[i + 1].isupper():
                merged_word += text[i + 1]
                i += 1
            else:
                merged_word += text[i + 1].upper()
                i += 1
        else:
            merged_word += text[i]
        i += 1
    return merged_word


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))
