import heapq


# min-heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heap)  # [1, 3, 4]

min_val = heapq.heappop(heap)  # 1

# max-heap uses negative values 
maxheap = []
heapq.heappush(maxheap, -3)
heapq.heappush(maxheap, -1)
heapq.heappush(maxheap, -4)
print(maxheap)

# | Operación                     | Tiempo   | Qué hace                                             |
# | ----------------------------- | -------- | ---------------------------------------------------- |
# | `insert(val)`                 | O(log n) | Añade y reajusta con **"heapify up"**                |
# | `extract_min` / `extract_max` | O(log n) | Saca el valor raíz y reajusta con **"heapify down"** |
# | `peek()`                      | O(1)     | Devuelve la raíz (mínimo o máximo)                   |
# | `heapify(arr)`                | O(n)     | Convierte un array a heap                            |
