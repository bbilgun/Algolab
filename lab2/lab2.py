# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# binary hailt recursive
def binary_search(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1

# Divide and Conquer
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return max(left_max, right_max)

arr = [34, 7, 23, 32, 5, 62]
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Merge Sort:", merge_sort(arr.copy()))
print("Binary Search for 23:", binary_search(arr, 23, 0, len(arr) - 1))
print("Maximum Value:", find_max(arr))
