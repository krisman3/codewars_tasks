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
    # for k in range(n_floors):
    #     tower[k] =
    #     tower.append('*' * (k * 2 + 1))

    # return tower

    for i in range(n_floors):
        if i == 0:
            tower.append('*')
        tower.append('*' * (i + 2))
    return tower


if __name__ == '__main__':
    print(tower_builder(6))
