"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains
only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.
"""


def find_uniq(arr):
    normalized = [''.join(set(word.lower().replace(" ", ""))) for word in arr]

    for word in arr:
        if normalized.count(''.join(set(word.lower().replace(" ", "")))) == 1:
            return word


if __name__ == "__main__":
    print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))  # => 'BbBb')
