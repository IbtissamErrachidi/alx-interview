#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island described in grid.

    Args:
    grid (list of list of int): 2D grid representing the island where
    1 represents land and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    def in_bounds(r, c):
        """Check if the position is within the grid boundaries."""
        return 0 <= r < rows and 0 <= c < cols
    
    def is_water_or_out_of_bounds(r, c):
        """Check if the position is water or out of bounds."""
        return not in_bounds(r, c) or grid[r][c] == 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check all four directions and add to perimeter
                if is_water_or_out_of_bounds(r - 1, c):  # Top
                    perimeter += 1
                if is_water_or_out_of_bounds(r + 1, c):  # Bottom
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c - 1):  # Left
                    perimeter += 1
                if is_water_or_out_of_bounds(r, c + 1):  # Right
                    perimeter += 1
    
    return perimeter

