from itertools import permutations

with open("data.txt", "r") as f:
    data = f.read().split('\n')

valid = 0

for x in data:
    x = x.split()
    if len(set(x)) == len(x):
        valid += 1

valid -= 2

for x in data:
    x = x.split()
    for word1 in x:
        cond = False
        for word2 in x:
            if sorted(list(word1)) == sorted(list(word2)):
                valid -= 1
                cond = True
                break
        if cond:
            break
print(valid)
