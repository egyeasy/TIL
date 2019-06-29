
def solve_naive(capacity, items, weights, values):  #180 seconds

    grid = [[0] * (capacity+1)]
    for item in range(items):
        grid.append(grid[item].copy())
        for k in range(weights[item], capacity+1):
            grid[item + 1][k] = max(grid[item][k], grid[item][k-weights[item]] + values[item])

    solution_value = grid[items][capacity]
    solution_weight = 0
    taken = []
    k = capacity
    for item in range(items, 0, -1):
        if grid[item][k] != grid[item-1][k]:
            taken.append(item - 1)
            k -= weights[item - 1]
            solution_weight += weights[item-1]

    return solution_value, solution_weight, taken


def solve_map(capacity, items, weights, values):  #102 seconds
    grid = [[0] * (capacity + 1)]
    for item in range(items):
        grid.append(grid[item].copy())
        this_weight = weights[item]
        this_value = values[item]

        grid[item + 1][this_weight:] = \
        list(map(lambda k: max(grid[item][k],
                               grid[item][k - this_weight] + this_value),
                 range(this_weight, capacity + 1)))

    solution_value = grid[items][capacity]
    solution_weight = 0
    taken = []
    k = capacity
    for item in range(items, 0, -1):
        if grid[item][k] != grid[item - 1][k]:
            taken.append(item - 1)
            k -= weights[item - 1]
            solution_weight += weights[item - 1]

    return solution_value, solution_weight, taken


def solve_list_comp(capacity, items, weights, values):  #81 seconds
    grid = [[0] * (capacity + 1)]
    for item in range(items):
        grid.append(grid[item].copy())
        this_weight = weights[item]
        this_value = values[item]

        grid[item + 1][this_weight:] = \
        [max(grid[item][k], grid[item][k - this_weight] + this_value)
         for k in range(this_weight, capacity + 1)]

    solution_value = grid[items][capacity]
    solution_weight = 0
    taken = []
    k = capacity
    for item in range(items, 0, -1):
        if grid[item][k] != grid[item - 1][k]:
            taken.append(item - 1)
            k -= weights[item - 1]
            solution_weight += weights[item - 1]

    return solution_value, solution_weight, taken