from collections import deque

queue = deque()
queue.append('Andi')
queue.append('Budi')
queue.append('Citra')
queue.append('Dina')
deque(['Andi','Budi','Citra','Dina'])

print('Antrian awal:', list(queue))
print('Yang pertama dilayani:', queue[0])
print('--- Mulai melayani ---')

nomor = 1
while queue:
    pelanggan = queue.popleft() 
    print(f'[{nomor}] Melayani: {pelanggan}')
    if queue:
        print(f' Antrian: {list(queue)}')
    nomor += 1
    
print('Semua pelanggan telah dilayani!')