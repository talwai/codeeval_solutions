grid = [ [None for x in range(4)] for y in range(4) ]


def count_paths (grid, x, y, w, h):
    if grid[x][y]:
    	return 0
    if x == w-1 and y == h-1:
    	return 1

    grid[x][y] = True
    count = 0
    if x > 0:
        count += count_paths (grid, x-1, y, w, h)
    if x < w - 1:
        count += count_paths (grid, x+1, y, w, h)
    if y > 0:
        count += count_paths (grid, x, y-1, w, h)
    if y < h - 1:
        count += count_paths (grid, x, y+1, w, h)

    grid[x][y] = False
    return count

WIDTH = 4
HEIGHT = 4

print count_paths(grid,0,0,WIDTH,HEIGHT)
