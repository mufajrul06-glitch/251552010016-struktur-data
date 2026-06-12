def counting_sort(arr):
    print("Input:", arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    print("Frekuensi (count array):")
    for i, C in enumerate(count):
        if C > 0:
            print(f"Angka {i}: {C} Kali")

    sortered_arr = []
    for i in range(len(count)):
        sortered_arr.extend([i] * count[i])

    print("Output (terurut):", sortered_arr)
    return sortered_arr
    
data = [5, 3, 8, 4, 2]
counting_sort(data)