import numpy as np
import networkx as nx


def shortest_path(graph, target):
    return nx.shortest_paths.dijkstra_path(
        graph,
        source=(0, 0),
        target=target,
        weight=weight_fn
    )


def weight_fn(_, end, __):
    global G
    return G.nodes[end]['risk']


def total_risk(graph, path):
    return sum(graph.nodes[pos]['risk'] for pos in path[1:])


def enlarge(grid, times=5):
    y_size, x_size = grid.shape
    enlarged = np.tile(grid, (5, 5))
    for tile_y in range(times):
        for tile_x in range(times):
            # Modify in place
            slice_y = slice(tile_y * y_size, (tile_y + 1) * y_size)
            slice_x = slice(tile_x * x_size, (tile_x + 1) * x_size)
            tile = enlarged[slice_y, slice_x]

            for _ in range(tile_y + tile_x):
                tile %= 9
                tile += 1

    return enlarged


def set_risks(graph, grid):
    for y, row in enumerate(grid):
        for x, risk in enumerate(row):
            graph.nodes[(x, y)]['risk'] = risk


if __name__ == '__main__':
    with open('input') as f:
        inp = f.read().splitlines()

    grid = np.array([list(row) for row in inp], dtype=np.uint8)
    big_grid = enlarge(grid)
    G = nx.grid_graph(big_grid.shape)
    set_risks(G, big_grid)

    target1 = (grid.shape[0] - 1, grid.shape[1] - 1)
    target2 = (big_grid.shape[0] - 1, big_grid.shape[1] - 1)
    print('Part 1:', total_risk(G, shortest_path(G, target1)))  # 361
    print('Part 2:', total_risk(G, shortest_path(G, target2)))  # 2838
