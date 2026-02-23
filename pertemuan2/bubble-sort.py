angka = [5, 3, 8, 2, 1]

for i in range(len(angka)):
 for j in range(len(angka)-i-1):
   if angka[j] > angka[j+1]:
    angka[j], angka[j+1] = angka[j+1], angka[j]

print("Hasil sorting:", angka) 