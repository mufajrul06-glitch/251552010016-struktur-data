def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"step {i + 1}: {arr}")

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)