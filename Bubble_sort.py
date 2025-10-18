def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", data)
sorted_data = bubble_sort(data)
print("Sorted array:", sorted_data)