from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # solo si no dirigido
    return graph


edges = [(0, 1), (0, 2), (1, 3)]
graph = build_graph(edges)

print(graph)
# Output: {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
