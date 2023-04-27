# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

# Write a program that simply outputs which cats have hats at the end.

def change_status(n: dict, z: int) -> dict:
    n.update([(z, int(not n.get(z)))])
    return n



l = []
cat_in_hat = 0
for i in range(1, 11):
    l.append(i)

dict = {}
dict = dict.fromkeys(tuple(l),1)

# print(change_status(dict, 1))

# print(dict)
def a():
    l = []
    # cat_in_hat = 0
    for i in range(1, 11):
        l.append(i)

    dict = {}
    dict = dict.fromkeys(tuple(l),0)
    for i in range(1, 11):
        for j in range(1, 11):
            if j%i == 0:
                change_status(dict, j)
    return dict

print(a())


# x = dict.update([(1,int(not(dict.get(1))))])


# print(x)