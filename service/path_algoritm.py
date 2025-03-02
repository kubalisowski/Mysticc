import math
import heapq

# Define the Cell class
class Cell:
    def __init__(self):
        # Parent cell's row and column index
        self.parent_y = 0
        self.parent_x = 0
        # Total cost (f = g + h)
        self.f = float('inf')
        # Cost from start to this cell
        self.g = float('inf')
        # Heuristic cost to destination
        self.h = 0


class AStarInfo():
    def __init__(self):
        self.GRID_ROW = 0  # Number of rows
        self.GRID_COL = 0  # Number of columns
        self.src      = [] # Start position
        self.dest     = [] # Destination

# Check if a cell is within the grid bounds
def is_valid(info, row, col):
    return 0 <= row < info.GRID_ROW and 0 <= col < info.GRID_COL

# Check if a cell is walkable
def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if we reached the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate Euclidean heuristic (h value)
def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)

# Trace and print the path from destination to source
def trace_path(cell_details, dest, debug = False):
    path = []
    row, col = dest

    while not (cell_details[row][col].parent_y == row and cell_details[row][col].parent_x == col):
        path.append((row, col))
        row, col = cell_details[row][col].parent_y, cell_details[row][col].parent_x

    path.append((row, col))  # Add source
    path.reverse()           # Reverse to get path from source to destination

    if (debug):
        for step in path: # list of tuples
            print("->", step, end=" ")
            
    return path

# Implement A* search
def a_star(info, grid, debug = False):
    # Extract source and destination coordinates
    src_y, src_x = info.src
    dest_y, dest_x = info.dest

    # Ensure the source and destination are valid
    if not is_valid(info, src_y, src_x) or not is_valid(info, dest_y, dest_x):
        return

    # Ensure the source and destination are walkable
    if not is_unblocked(grid, src_y, src_x) or not is_unblocked(grid, dest_y, dest_x):
        return

    # Check if source is already the destination
    if is_destination(src_y, src_x, info.dest):
        return

    # Initialize visited cells
    closed_list = [[False for _ in range(info.GRID_COL)] for _ in range(info.GRID_ROW)]

    # Initialize cell details
    cell_details = [[Cell() for _ in range(info.GRID_COL)] for _ in range(info.GRID_ROW)]

    # Initialize source cell details
    cell_details[src_y][src_x].f = 0
    cell_details[src_y][src_x].g = 0
    cell_details[src_y][src_x].h = 0
    cell_details[src_y][src_x].parent_y = src_y
    cell_details[src_y][src_x].parent_x = src_x

    # Open list (priority queue for A* search)
    open_list = []
    heapq.heappush(open_list, (0.0, src_y, src_x))

    found_dest = False  # Flag to check if path is found

    # A* search loop
    while open_list:
        # Extract the cell with the lowest f-value
        _, y, x = heapq.heappop(open_list)
        closed_list[y][x] = True  # Mark cell as visited

        # Define movement directions (4-way movement)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Uncomment for diagonal movement:
        # directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Explore all adjacent cells
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            # Check if the neighbor is within bounds and walkable
            if is_valid(info, new_y, new_x) and is_unblocked(grid, new_y, new_x) and not closed_list[new_y][new_x]:
                # If it's the destination, reconstruct and return path
                if is_destination(new_y, new_x, info.dest):
                    cell_details[new_y][new_x].parent_y = y
                    cell_details[new_y][new_x].parent_x = x
                    found_dest = True
                    return trace_path(cell_details, info.dest, debug)

                # Compute new f, g, and h values
                g_new = cell_details[y][x].g + 1.0
                h_new = calculate_h_value(new_y, new_x, info.dest)
                f_new = g_new + h_new

                # If this path is better, update the cell details
                if cell_details[new_y][new_x].f == float('inf') or cell_details[new_y][new_x].f > f_new:
                    heapq.heappush(open_list, (f_new, new_y, new_x))
                    cell_details[new_y][new_x].f = f_new
                    cell_details[new_y][new_x].g = g_new
                    cell_details[new_y][new_x].h = h_new
                    cell_details[new_y][new_x].parent_y = y
                    cell_details[new_y][new_x].parent_x = x

    # If we exit the loop without finding the destination
    if not found_dest:
        raise ValueError("AStar: Failed to find the destination.")


### DEBUG ###
def main():
    # 1: walkable, 0: blocked
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Initialize cell grid size
    info = AStarInfo()
    info.GRID_ROW = len(grid)     # Number of rows
    info.GRID_COL = len(grid[0])  # Number of columns
    info.src      = [8, 0]        # Start position
    info.dest     = [0, 0]        # End position

    # Run A* search
    a_star(info, grid, True)

main()
