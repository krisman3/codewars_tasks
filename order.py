"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position
the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive
numbers.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->
"""


def order(sentence: str):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = []

    for word in words:
        for chr in word:
            if chr.isdigit():
                index = int(chr) - 1
                sorted_words.insert(index, word)
                break

    sorted_words = [word for word in sorted_words if word is not None]

    return " ".join(sorted_words)


if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))