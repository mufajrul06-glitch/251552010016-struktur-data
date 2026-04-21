piring = []
print ('awal:', piring)

piring.append('biru')
piring.append('putih')
piring.append('coklat')
print ('setelah push:', piring)

top = piring[0]
print ('peek:', top)

popped = piring.pop()
print ('Dipop:', popped)
print ('Piring', piring)

print ('kosong?', len (piring) ==0)
print ('ukuran:', len (piring))