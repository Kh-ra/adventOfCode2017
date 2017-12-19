# Get the dimensions of the data.
rows = int(input("How many rows: "))
cols = int(input("How many columns: "))

# Read in the data to a single list.
with open("matrix.txt", "r") as f:
    data = list(map(int, f.read().split()))

# Note length of the data.
length = len(data)

# Create sums for Part 1 and Part 2
part1 = 0
part2 = 0

# Iterate over the rows in the matrix
for rowIndex in range(rows):

    # Create a sublist that is only the elements from the current row
    row = data[(cols*rowIndex):(cols*(rowIndex+1))]
    
    # Add to part1
    part1 += max(row) - min(row)        
   
    # Iterate over row for each element twice
    for x in row:
        for y in row:

            # If they aren't the same element and float division yields the same result as integer division than they divide
            if (x/y == x//y and x != y):

                # Add to part2
                part2 += (x//y)

print("Part 1:", part1)
print("Part 2:", part2)
