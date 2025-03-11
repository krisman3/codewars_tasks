"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!"""


def find_missing(chars: str):
    chars_str = ''.join(chars).lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alph_char = alphabet.index(chars_str[0])

    for i in range(len(chars_str)):
        if chars_str[i] != alphabet[alph_char]:
            if chars[0].isupper():
                return alphabet[alph_char].upper()
            else:
                return alphabet[alph_char]
        alph_char += 1


if __name__ == "__main__":
    print(find_missing(['O','Q','R','S']))
