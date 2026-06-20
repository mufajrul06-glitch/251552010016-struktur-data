def interpolation_search(arr, key):
    low = 0
    high = len(arr)-1

    while low <= high and arr[low] <= key <= arr[high]:
        pos = low + ((key - arr[low]) * (high - low)) // ((arr[high] - arr[low]))
        if pos < 0 or pos >= len(arr):
            return -1
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

data = [10, 20, 30, 40, 50]
print(f"Array saat ini: {data}")
cari = int(input("Masukan angka yang ingin dicari: "))
hasil = interpolation_search(data, cari)

if hasil != -1:
    print(f"Angka ditemukan di indeks: {hasil}")
else:
    print("Angka tidak ditemukan dalam array")