def has_cycle_directed(graph):
    visited = set()
    recStack = set()

    def dfs(node):
        print(f"\nEntrando a {node}")
        visited.add(node)
        recStack.add(node)
        print(f"  visited: {visited}")
        print(f"  recStack: {recStack}")

        for neighbor in graph[node]:
            print(f"    {node} → {neighbor}")
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recStack:
                print(f"    ⚠️ Ciclo detectado: {neighbor} está en recStack")
                return True

        # Aquí se remueve de recStack porque ya salimos del nodo
        print(f"  Saliendo de {node}, eliminando de recStack")
        recStack.remove(node)
        print(f"  recStack actual: {recStack}")
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


graph = {0: [1], 1: [2], 2: [0]}


print(has_cycle_directed(graph))
