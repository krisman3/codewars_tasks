"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
"""


def tower_builder(n_floors):
    tower = [] * n_floors

    for i in range(n_floors):
        asterisks = '*' * (i * 2 + 1)
        spaces = ' ' * (n_floors - i - 1)
        tower.append(spaces + asterisks + spaces)

    return tower


if __name__ == '__main__':
    print(tower_builder(10))
