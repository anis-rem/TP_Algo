import random

list = random.sample(range(1, 100), 10)
print("Liste non triée :", list)

def tri_tas(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        tri_tas(arr, n, largest)

def get_array_parameters(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        tri_tas(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        tri_tas(arr, i, 0)

    return arr
sorted_list = get_array_parameters(list[:])


sorted_list.reverse()

print("Liste triée (décroissante) :", sorted_list)
