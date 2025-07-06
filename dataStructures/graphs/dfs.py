def dfs(node, visited, graph):
    # print("S:",node)
    if node in visited:
        return
    visited.add(node)
    print(node, graph[node])  # o hacer algo con el nodo

    for neighbor in graph[node]:
        dfs(neighbor, visited, graph)


#     0
#    / \
#   1   2
#   |
#   3


graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}

# Uso:
visited = set()
dfs(0, visited, graph)
