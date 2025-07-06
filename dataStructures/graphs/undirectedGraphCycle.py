from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # solo si no dirigido
    return graph


def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            # print(neighbor)
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


edges = [
    (0, 1),
    (1, 2),
]
graph = build_graph(edges)

graphEquivalent = {0: [1], 1: [2], 2: [0]}  # ciclo: 0 → 1 → 2 → 0

graph2 = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 1],  # hay una vuelta a 1 sin que sea su padre
}


# print(graph)
print(graphEquivalent)

print(has_cycle_undirected(graphEquivalent))
print(has_cycle_undirected(graph2))
