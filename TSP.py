from itertools import permutations
def tsp_brute_force(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_route = []
    for perm in permutations(vertices):
        current_weight = 0
        k = start
        route = [start]
        for j in perm:
            current_weight += graph[k][j]
            route.append(j)
            k = j
        current_weight += graph[k][start]  
        route.append(start)
        if current_weight < min_path:
            min_path = current_weight
            best_route = route
    return min_path, best_route
graph = {
    0: {0: 0, 1: 10, 2: 15, 3: 20},
    1: {0: 10, 1: 0, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 2: 0, 3: 30},
    3: {0: 20, 1: 25, 2: 30, 3: 0}
}
cost, path = tsp_brute_force(graph, 0)
print("Minimum cost:", cost)
print("Best route:", path)