from collections import deque
queue = deque()
queue.append('sapu')
queue.append('sapi')
queue.append('sapa')
print('queue:', queue)

front = queue[0]
print('peek:', front)

keluar = queue.popleft()
print('dequeue:', keluar)
print('queue:', queue)

print('kosong?', len(queue) == 0)
print('ukuran:', len(queue))