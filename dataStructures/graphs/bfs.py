from collections import deque


def bfs(start, graph):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(node)  # o hacer algo con el nodo
        for neighbor in graph[node]:
            queue.append(neighbor)


#     0
#    / \
#   1   2
#   |
#   3

graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}

# Uso:
bfs(0, graph)
