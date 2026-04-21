import heapq

pq = []

heapq.heappush(pq, (3, 'task C - rendah'))
heapq.heappush(pq, (1, 'task A - tinggi'))
heapq.heappush(pq, (2, 'task B - sedang'))

print('priority queue:', pq)

while pq:
    prioritas, task = heapq.heappop(pq)
    print(f'[prioritas {prioritas}] proses: {task}')