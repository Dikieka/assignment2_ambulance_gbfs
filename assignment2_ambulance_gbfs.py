import heapq
import time  

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def find(grid, symbol):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == symbol:
                return (i, j)

def get_neighbors(pos, grid):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dx, dy in dirs:
        x, y = pos[0]+dx, pos[1]+dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "T":
            neighbors.append((x, y))
    return neighbors

def gbfs(grid, start, goal):
    open_set = [(manhattan(start, goal), start)]
    came_from = {}
    visited = {start}
    node_count = 1  

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct(came_from, start, goal), node_count

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_set, (manhattan(neighbor, goal), neighbor))
                node_count += 1  
    return None, node_count

def reconstruct(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

def print_grid(grid, path):
    grid_copy = [row[:] for row in grid]
    for x, y in path:
        if grid_copy[x][y] not in "SH":
            grid_copy[x][y] = "*"
    for row in grid_copy:
        print("".join(row))

def run_assignment2():
    grid = [
        list("S...T"),
        list(".T.T."),
        list("....."),
        list("T.T.."),
        list("..H..")
    ]
    start = find(grid, "S")
    goal = find(grid, "H")
    
    start_time = time.time()

    path, node_count = gbfs(grid, start, goal)
    
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000

    print("\nAssignment 2 - GBFS Path (Ambulance Dispatch):")
    if path:
        print_grid(grid, path)
    else:
        print("No path found.")
    
    print(f"Execution Time: {execution_time:.4f} ms")
    print(f"Nodes Explored: {node_count}")