# Q15. There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green.
# Blue represents the sea, and green represents the land. When two green squares are in contact with
# the top and bottom, or right and left, they are said to be ground. The area created by only one green
# square is called island. For example, there are five islands in the figure below. Write a Python
# program to read the mass data and find the number of islands.

# Read the 10 x 10 grid
grid = []

print("Enter 10 rows containing 0 and 1:")

for _ in range(10):
    row = list(map(int, input().split()))
    grid.append(row)


def explore_island(row, col):
    # Stop if the position is outside the grid
    if row < 0 or row >= 10 or col < 0 or col >= 10:
        return

    # Stop if the square is sea or already visited
    if grid[row][col] == 0:
        return

    # Mark the current land square as visited
    grid[row][col] = 0

    # Explore the four neighbouring squares
    explore_island(row - 1, col)  # Up
    explore_island(row + 1, col)  # Down
    explore_island(row, col - 1)  # Left
    explore_island(row, col + 1)  # Right


island_count = 0

for row in range(10):
    for col in range(10):
        if grid[row][col] == 1:
            island_count += 1
            explore_island(row, col)

print("Number of islands:", island_count)