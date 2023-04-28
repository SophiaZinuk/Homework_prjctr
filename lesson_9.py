# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

# Write a program that simply outputs which cats have hats at the end.

""" 
According to the given dictionary and key, 
we change the corresponding factorial value to the opposite
"""


def change_status(n: dict, z: int) -> dict:
    n.update([(z, int(not n.get(z)))])
    return n


def print_cats_with_hats(number_of_cats: int, number_of_rounds: int) -> list:
    keys_list = []
    # generate a list of cat numbers
    for i in range(1, number_of_cats + 1):
        keys_list.append(i)

    # created a dictionary with keys - numbers of cats and values - 0 (cat without a hat)
    dict = {}
    dict = dict.fromkeys(tuple(keys_list), 0)

    # we go through all rounds of the game with an outer loop. we go through the 
    # numbers of all the cats in an inner loop and, according to the round, 
    # change the values in the dictionary
    for i in range(1, number_of_rounds + 1):
        for j in range(1, number_of_cats + 1):
            if j % i == 0:
                change_status(dict, j)

    # we check the resulting dictionary values, 
    # and output those keys where the value is equal to one           
    list_of_cats_with_hats = []
    result = tuple(dict.values())
    for i in range(len(result)):
        if result[i] == 1:
            list_of_cats_with_hats.append(i+1)
    return list_of_cats_with_hats


print(print_cats_with_hats(1000, 1000))
