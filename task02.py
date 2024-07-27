def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] == x:
            return (iterations, arr[mid])
 
        elif arr[mid] < x:
            low = mid+ 1
 
        else:
            high = mid - 1
    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = "Cant found"

    return (iterations, upper_bound)

arr = [2.5, 3.4, 4.6, 10.11, 40.34]

iterations, upper_bound = binary_search(arr, 11.6)
print(f"Ітерації: {iterations}, верхня межа: {upper_bound}")

 