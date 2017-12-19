# Read in the input as a list of integers.
data = list(map(int, list(input())))

# Take note of length of input.
length = len(data)

# Get the offset of half the list for Part 2.
offset = length//2

# Create sums for Part 1 and Part 2 of the test.
part1 = 0
part2 = 0

# Iterate over the data.
for index in range(length):

    # Calculate Part 1: Check if digit matches next digit.
    if data[index] == data[(index+1) % length]:
        part1 += data[index]

    # Calculate Part 2: Check if digit opposite in the list matches.
    if data[index] == data[(index + offset) % length]:
        part2 += data[index]

print("Part 1:", part1)
print("Part 2:", part2)
