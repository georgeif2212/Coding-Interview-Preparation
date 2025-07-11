import heapq
heap = []                     
heapq.heappush(heap, 3)       # inserta 3
x = heapq.heappop(heap)       # saca el menor

heapq.heappush(heap, -x)      # para max heap: guarda negativos
-x = heapq.heappop(heap)      # y luego invierte signo


from itertools import permutations, combinations
permutations([1,2,3])         # todas las permutaciones
combinations([1,2,3], 2)      # combinaciones de 2 elementos
