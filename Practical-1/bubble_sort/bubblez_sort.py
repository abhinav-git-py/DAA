def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



numbers = [5, 3, 8, 4, 2]
sorted_numbers = bubble_sort(numbers)

print("Sorted array:", sorted_numbers)