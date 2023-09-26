#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    if not grid:
        return 0
    perimeter = 0

    row, cols = len(grid), len(grid[0])
    for i in range():
        for j in range(cols[row]):
            if grid[row][cols] == 1:
                perimeter += 4
                if i > 0 and grid[row-1][cols] == 1:
                    perimeter -= 2
                if j > 0 and grid[row][cols-1] == 1:
                    perimeter -= 2
    return perimeter


# def island_perimeter(grid):
#     if not grid:
#         return 0

#     perimeter = 0
    # rows, cols = len(grid), len(grid[0])

    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 1:
    #             perimeter += 4  # Start with 4 sides for each land cell

    #             # Check adjacent cells (up, down, left, and right)
    #             if row > 0 and grid[row - 1][col] == 1:
    #                 perimeter -= 2
    #             # if row < rows - 1 and grid[row + 1][col] == 1:
    #             #     perimeter -= 1
    #             if col > 0 and grid[row][col - 1] == 1:
    #                 perimeter -= 2
    #             # if col < cols - 1 and grid[row][col + 1] == 1:
    #             #     perimeter -= 1

    # return perimeter
